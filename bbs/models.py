from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)         # 제목
    author = models.CharField(max_length=10)        # 작성자
    content = models.TextField(max_length=300)      # 내용
    date = models.DateTimeField(auto_now_add=True)  # 작성일

    def __str__(self):
        return self.title