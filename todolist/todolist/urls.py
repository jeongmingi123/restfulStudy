from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),    # app

    path('todo_api/', include('todo_api.urls')),    # api
]
