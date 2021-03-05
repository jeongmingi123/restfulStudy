from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from posts.views import PostViewSet


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

app_name = 'api'

router.register(r'posts', PostViewSet, basename='posts')
urlpatterns = router.urls

urlpatterns += [
    path('users/', include('users.urls', namespace='users')),
]
