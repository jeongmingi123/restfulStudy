from django.urls import path
from . import views

app_name = 'bbs'
urlpatterns = [
    path('', views.ListData, name='list'),
    path('<int:key>/', views.DetailData, name='detail'),
    path('post/', views.PostData, name='post'),
    path('delete/', views.DeleteData, name='delete')
]