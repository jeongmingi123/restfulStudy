from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from model_bakery import baker

User = get_user_model()


class AuthTest(APITestCase):
    def setUp(self):
        self.username, self.password = 'testuesr', 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password, email='test@test.com')
        self.url = reverse('api:users:obtain-auth-token')

    def test_token_auth(self):
        res = self.client.post(self.url, {
            'username': self.username,
            'password': self.password,
        })
        token = Token.objects.get(user=self.user)

        self.assertEqual(res.data['token'], token.key)
