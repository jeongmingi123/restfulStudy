from django.urls import path
from .views import TodoList, TodoCreate, todo_update, todo_delete

app_name = 'todo'
urlpatterns = [
    path('', TodoList.as_view(), name='list'),
    path('create/', TodoCreate.as_view(), name='create'),
    path('<str:pk>/update/', todo_update, name='update'),
    path('<str:pk>/delete/', todo_delete, name='delete'),
]

