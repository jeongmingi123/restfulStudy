from http import HTTPStatus

from django.test import TestCase
from django.shortcuts import reverse
from rest_framework.test import APITestCase
from model_bakery import baker

from posts.models import Post

# Create your tests here.
