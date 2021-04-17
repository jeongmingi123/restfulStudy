from django import forms
from .models import Todo
from datetime import date


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = {'item'}


