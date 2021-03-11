from django.urls import path
from . import views

# /blog/
urlpatterns = [
    path('', views.index),
    path('post_list/', views.post_list, name='list'),
    path('post_get/', views.post_get),
    path('post_create/', views.post_create, name='create'),
    path('post_delete/', views.post_delete),
]