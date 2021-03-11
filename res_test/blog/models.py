from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
