from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'user', 'content']


admin.site.register(Post, PostAdmin)
