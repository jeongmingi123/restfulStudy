from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthenticatedAndChangedOwned


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.visible_objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        '''
        permissions for Posts

        list, retrieve: AllowAny
        create: IsAuthenticated
        update: Created user
        destroy: Created user, admin user
        '''
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticatedAndChangedOwned]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer, **kwargs):
        return serializer.save(user=self.request.user)
