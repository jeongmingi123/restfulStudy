from django.contrib import admin
from . import models


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = (
        '__str__',
        'created',
        'text',
        'comment',
    )