from django.urls import path
from rest_framework.authtoken import views


app_name = 'users'
urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token, name='obtain-auth-token'),
]
