from django.urls import path
from .views import *


app_name = 'posts'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('posts/create/', PostCreateView.as_view(), name='create'),
    path('posts/delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
]
