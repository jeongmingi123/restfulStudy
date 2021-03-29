from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from django.views import View


class PostListView(View):
    def get(self, request):
        posts = Post.objects.all().order_by('-created_at')
        return HttpResponse(posts)


class PostDetailView(View):
    def get(self, request, pk):
        posts = Post.objects.get(pk=pk)
        return HttpResponse(posts)


@method_decorator(csrf_exempt, name='dispatch')
class PostCreateView(View):
    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')

        posts = Post.objects.create(title=title, content=content)
        return HttpResponse(posts)


@method_decorator(csrf_exempt, name='dispatch')
class PostDeleteView(View):
    def post(self, request, pk):
        posts = Post.objects.get(pk=pk)
        posts.delete()
        return HttpResponse(posts)
