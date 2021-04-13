from django import forms
from .models import Todo
from datetime import date


class TodoForm(forms.Form):
    item = forms.CharField(label='item', widget=forms.TextInput(attrs={'placeholder': 'item'}), required=True)
