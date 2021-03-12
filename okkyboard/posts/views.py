from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Post, User
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


# FBV -> View (CBV) -> APIView, GenericView (mixin) -> ViewSet
from django.http import HttpResponse


def post_list(request):
    title_lists = Post.objects.values_list('title', flat=True)
    posts_titles = ','.join(title_lists)
    return HttpResponse(posts_titles)


def post_detail(requst, pk):
    post = Post.objects.get(pk=pk)
    return HttpResponse(post.title)


@csrf_exempt
def post_create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    post = Post.objects.create(title=title, content=content, user=User.objects.last())
    return HttpResponse(post.title)


@csrf_exempt
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return HttpResponse()


