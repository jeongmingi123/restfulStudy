from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from .models import Post


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return HttpResponse(posts)


def post_detail(request, pk):
    posts = Post.objects.get(pk=pk)
    return HttpResponse(posts)


@csrf_protect
def post_create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    posts = Post.objects.create(title=title, content=content)
    return HttpResponse(posts)


@csrf_protect
def post_delete(request, pk):
    posts = Post.objects.get(pk=pk)
    posts.delete()
    return HttpResponse(posts)
