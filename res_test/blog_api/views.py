from rest_framework import viewsets
from blog.models import Post
from blog.serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
