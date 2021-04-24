from django.contrib.auth.models import User, Group
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework import permissions
from .models import Post


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

