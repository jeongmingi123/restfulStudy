from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
