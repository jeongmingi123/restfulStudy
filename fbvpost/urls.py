from django.urls import path
from .views import *


app_name = 'posts'

urlpatterns = [
    path('posts/', post_list, name='list'),
    path('<int:pk>/', post_detail, name='detail'),
    path('posts/create/', post_create, name='create'),
    path('posts/delete/<int:pk>/', post_delete, name='delete'),
]
