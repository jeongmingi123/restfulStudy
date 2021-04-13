from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from datetime import timezone

from .models import Todo
from .form import TodoForm


class TodoFormCreate(FormView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/todo_form.html"
    success_url = reverse_lazy('todo_list')



class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/todo_create.html"
    success_url = reverse_lazy('todo_list')



class TodoListView(ListView):
    model = Todo
    success_url = reverse_lazy('todo_list')
    context_object_name = "todos"
    template_name = "todo/todo_list.html"


class TodoDeleteView(DeleteView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('blog_list')
    template_name = "todo/todo_delete.html"
