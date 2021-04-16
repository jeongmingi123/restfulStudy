from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    fields = ['title', 'check']
    list_display = ('title', 'check', 'create_dt')


admin.site.register(Todo, TodoAdmin)