from django.urls import path, include
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
]
