from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from quickstart import views
from blog.views import all_blog as blog_views
from blog.views import bloging, new_blog


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'post', views.PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('blog/', blog_views, name='blog'),
    path('blog/<int:pk>', bloging, name="bloging"),
    path('blog/new_blog', new_blog, name="new_blog")

]
