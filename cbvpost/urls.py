from django.urls import path
from .views import *


app_name = 'cbvposts'

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
]
