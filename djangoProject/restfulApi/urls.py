from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from quickstart import views
from blog.views import Blog_list
from blog.views import BlogDetail, New_blog, Remove_blog, Edit_blog

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'post', views.PostViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('blog_list/', Blog_list.as_view(), name='blog_list'),
    path('blog/<int:pk>', BlogDetail.as_view()),
    path('blog/new_blog', New_blog.as_view(), name="new_blog"),
    path('blog/<int:pk>/remove/', Remove_blog.as_view()),
    path('blog/<int:pk>/edit/', Edit_blog.as_view())

]
