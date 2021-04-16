from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Todo


class TodoList(ListView):
    model = Todo
    ordering = ['-create_dt']


class TodoCreate(CreateView):
    model = Todo
    fields = ['title']

    def get_success_url(self):
        return reverse('todo:list')


def todo_update(request, pk):
    todo = Todo.objects.get(id=int(pk))

    if todo.check:
        todo.check = False
    else:
        todo.check = True
    todo.save()

    todos = Todo.objects.all().order_by('-create_dt')
    context = {'object_list': todos}

    return render(request, 'todo/todo_list.html', context)


def todo_delete(request, pk):
    todo = Todo.objects.get(id=int(pk))
    todo.delete()

    todos = Todo.objects.all().order_by('-create_dt')
    context = {'object_list': todos}

    return render(request, 'todo/todo_list.html', context)
