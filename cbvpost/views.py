from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post
from django.views import generic


class PostListView(generic.ListView):
    model = Post
    template_name = 'list.html'
    context_object_name = 'posts'


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'target_post'
    template_name = 'detail.html'


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('cbvposts:list')
    template_name = 'create.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('cbvposts:list')
    template_name = 'delete.html'
