from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(verbose_name='생성날짜', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='수정날짜', auto_now=True)

    class Meta:
        abstract = True


class VisiblePostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_visible=True)


class Post(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_visible = models.BooleanField(default=True)

    objects = models.Manager()
    visible_objects = VisiblePostManager()

    class Meta:
        ordering = ['created_at']
        verbose_name = '게시글'

    def __str__(self):
        return self.title
