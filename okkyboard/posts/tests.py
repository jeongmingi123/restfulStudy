from django.test import TestCase
from model_bakery import baker

from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        self.post = baker.make('posts.Post')

    def test_isinstance_post(self):
        self.assertIsInstance(self.post, Post)

