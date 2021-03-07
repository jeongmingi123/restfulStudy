from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    # id (게시글 번호) => 장고 제공 기본키 적용
    # title (게시글 제목)
    title = models.CharField(max_length=255)
    # user (작성자 - 외래키 지정)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # create_dt (작성일자)
    create_dt = models.DateTimeField(auto_now_add=True)
    # modify_dt (수정일자)
    modify_dt = models.DateTimeField(auto_now=True)
    # content (내용)
    content = models.TextField()

    def __str__(self):
        return self.title
