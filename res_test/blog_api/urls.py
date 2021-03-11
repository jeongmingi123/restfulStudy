from django.conf.urls import url, include
from rest_framework import routers
from .views import BlogViewSet


router = routers.DefaultRouter()
router.register('blog', BlogViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]