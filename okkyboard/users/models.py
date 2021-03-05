from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField('닉네임', max_length=20, blank=True, default="")

    class Meta:
        verbose_name = '회원'
        verbose_name_plural = '회원'
