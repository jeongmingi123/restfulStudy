from django.conf.urls import url, include
from rest_framework import routers
from .views import TodoViewSet

router = routers.DefaultRouter()
router.register('todo', TodoViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]