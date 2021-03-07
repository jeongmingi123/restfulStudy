from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from study_board.views import StudyBoardViewSet

router = routers.DefaultRouter()
router.register('study_board', StudyBoardViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
