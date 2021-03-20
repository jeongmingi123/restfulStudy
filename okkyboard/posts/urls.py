from django.urls import path
from rest_framework.authtoken import views
from .views import *


app_name = 'posts'
urlpatterns = [
    path('posts/', post_list, name='list'),
    path('post/<int:pk>/', post_detail, name='detail'),
    path('posts/create/', post_create, name='create'),
    path('posts/delete/<int:pk>/', post_delete, name='delete'),
    path('cbv/posts/', PostListView.as_view(), name='cbv-list'),
    path('cbv/posts/<int:pk>/', PostDetailView.as_view(), name='cbv-detail'),
    path('cbv/posts/create/', PostCreateView.as_view(), name='cbv-create'),
    path('cbv/posts/delete/<int:pk>/', PostDeleteView.as_view(), name='cbv-delete'),
]
