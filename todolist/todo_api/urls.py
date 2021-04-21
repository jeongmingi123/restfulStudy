from django.urls import path
from . import views

urlpatterns = [
    # todo
    # GET - list
    # POST - create
    path('todo/', views.todo),

    # todo/99
    # GET - detail
    # PUT - update
    # DELETE - delete
    path('todo/<int:pk>', views.todo_get_put_delete),
]