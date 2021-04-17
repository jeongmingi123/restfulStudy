from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from datetime import timezone
from .models import Todo
from .form import TodoForm


class TodoListView(ListView):
    model = Todo
    success_url = reverse_lazy('todo_list')
    context_object_name = "todo_list"
    template_name = "todo/todo_list.html"


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')


class TodoDeleteView(DeleteView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')
    template_name = "todo/todo_delete.html"


class TodoEditView(UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')
    template_name = "todo/todo_edit.html"

