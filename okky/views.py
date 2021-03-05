from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework import permissions


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)