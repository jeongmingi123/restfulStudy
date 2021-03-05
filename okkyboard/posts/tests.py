from http import HTTPStatus

from django.shortcuts import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from model_bakery import baker

from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        self.post = baker.make('posts.Post')

    def test_isinstance_post(self):
        self.assertIsInstance(self.post, Post)


class PostViewSetTest(APITestCase):
    def setUp(self):
        self.user = baker.make('users.User')
        self.list_url = reverse('api:posts-list')
        self.post = baker.make('posts.Post', user=self.user)
        self.detail_url = reverse('api:posts-detail', kwargs={'pk': self.post.id})

    def test_list_pi_url_works(self):
        res = self.client.get(self.list_url)

        self.assertEqual(res.status_code, HTTPStatus.OK)
        self.assertEqual(len(res.data), 1)

    def test_detail_api_url_works(self):
        res = self.client.get(self.detail_url)

        self.assertEqual(res.status_code, HTTPStatus.OK)
        self.assertEqual(list(res.data.keys()), ['id', 'user', 'title', 'content', 'created_at' ,'updated_at'])

    def test_create_api_url_without_user(self):
        '''post 만들때 로그인 안한 유저는 401'''
        res = self.client.post(self.list_url, {
            'title': 'test',
            'content': 'test',
        })

        self.assertEqual(res.status_code, HTTPStatus.UNAUTHORIZED)

    def test_create_api_works(self):
        self.client.force_authenticate(self.user)
        TITLE = 'test title'
        res = self.client.post(self.list_url, {
            'title': TITLE,
            'content': 'test',
        })

        self.assertEqual(res.status_code, HTTPStatus.CREATED)
        self.assertEqual(res.data['title'], TITLE)

        # 만들어진 post가 해당 유저의 것인지 확인
        post = Post.objects.last()
        self.assertEqual(post.user, self.user)

    def test_update_api_without_user(self):
        '''post 업데이트시 로그인 안한 유저는 401'''
        res = self.client.patch(self.detail_url, {
            'content': 'updated',
        })

        self.assertEqual(res.status_code, HTTPStatus.UNAUTHORIZED)

    def test_update_api_with_invalid_user(self):
        '''다른 유저의 글을 업데이트시 403'''
        new_user = baker.make('users.User')
        self.client.force_authenticate(new_user)
        res = self.client.patch(self.detail_url, {
            'content': 'updated',
        })

        self.assertEqual(res.status_code, HTTPStatus.FORBIDDEN)

    def test_update_api_works(self):
        '''다른 유저의 글을 업데이트시 403'''
        self.client.force_authenticate(self.user)
        UPDATED_CONTENT = 'updated'
        res = self.client.patch(self.detail_url, {
            'content': UPDATED_CONTENT,
        })

        self.assertEqual(res.status_code, HTTPStatus.OK)
        self.assertEqual(res.data['content'], UPDATED_CONTENT)

    def test_destroy_api_without_login(self):
        '''로그인 안하고 글 지우면 401'''
        res = self.client.delete(self.detail_url)

        self.assertEqual(res.status_code, HTTPStatus.UNAUTHORIZED)

    def test_destroy_api_with_invalid_user(self):
        '''다른 유저의 글을 제거시 403'''
        new_user = baker.make('users.User')
        self.client.force_authenticate(new_user)
        res = self.client.delete(self.detail_url)

        self.assertEqual(res.status_code, HTTPStatus.FORBIDDEN)

    def test_destroy_api_url_works(self):
        self.client.force_authenticate(self.user)
        res = self.client.delete(self.detail_url)

        self.assertEqual(res.status_code, HTTPStatus.NO_CONTENT)
        self.assertFalse(Post.objects.filter(pk=self.post.id).exists())
