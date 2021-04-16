from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from .forms import PostForm
from .models import Post


# -------------------------------------------
# Generic View

# post list
class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'


# post detail
class PostDetail(DetailView):
    model = Post
    # context_object_name = 'post'
    template_name = 'blog/post_detail.html'


# post create
class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')


# post update
class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')


# post delete
class PostDelete(DeleteView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')


# -------------------------------------------

# 이전 CBV with View 코드


# # 포스트 목록 보기 - GET
# class PostList(View):
#
#     def get(self, request):
#         posts = Post.objects.all()
#         context = {'posts': posts}
#         return render(request, 'blog/post_list.html', context)
#
#
# # 특정 포스트 보기 - GET
# class PostDetail(View):
#
#     def get(self, request, post_id):
#         post = Post.objects.get(id=post_id)
#         context = {'post': post}
#         return render(request, 'blog/post_detail.html', context)
#
#
# # 포스트 생성하기 - GET: page / POST: create & redirect
# @method_decorator(csrf_exempt, name='dispatch')
# class PostCreate(View):
#
#     def get(self, request):
#         return render(request, 'blog/post_create.html', dict())
#
#     def post(self, request):
#         post = Post()  # .objects.create('')
#         post.title = request.POST['title']
#         post.user = User.objects.get_by_natural_key(request.POST['username'])
#         post.content = request.POST['content']
#         post.save()
#         return redirect('blog:post_list')
#
#
# # 특정 포스트 수정 - GET / POST
# class PostUpdate(View):
#
#     def get(self, request, post_id):
#         post = Post.objects.get(id=post_id)
#         context = {'post': post}
#         return render(request, 'blog/post_update.html', context)
#
#     def post(self, request):
#         post_id = request.POST['post_id']
#         post = Post.objects.get(id=post_id)
#         post.content = request.POST['content']
#         post.save()
#         return redirect('blog:post_detail', post_id=post_id)
#
#
# # 특정 포스트 삭제 - GET
# class PostDelete(View):
#
#     def get(self, request, post_id):
#         post = Post.objects.get(id=post_id)
#         post.delete()
#         return redirect('blog:post_list')


# -------------------------------------------

# 이전 FBV 코드

    # def index(self, request):
    #     html = '''
    #            <h3>FBV, HttpResponse Test</h3>
    #            <a href='/blog/post_list'>리스트페이지 이동</a>
    #            '''
    #     header_test = {
    #         'h1': 1,
    #         'h2': 'str',
    #         'h3': []
    #     }
    #     response = HttpResponse()
    #     for k, v in header_test.items():
    #         response.setdefault(k, v)
    #     response.write(html)
    #     return response
    #
    #
    # def post_list(request):
    #     response = HttpResponse()
    #     posts = Post.objects.all()
    #     html = ''
    #     urls = '''
    #            <a href='/blog/post_create/'>create 이동</a><br/>
    #            '''
    #     p_info = []
    #     for post in posts:
    #         p_info.append("# %s / "
    #                       "%s / "
    #                       "<a href='/blog/post_get/?post_id=%d'>'%s'</a> / "
    #                       "[%s] / "
    #                       % (post.id, post.user.username, post.id, post.title, post.create_dt))
    #     html += '<br/>'.join(p_info)
    #     html += '''<br/><br/>
    #             <h3>포스트 삭제</h3>
    #             <form action="/blog/post_delete/" method="GET">
    #             <input type="number" name="post_id">
    #             <input type="submit" value="삭제">
    #             </form>
    #             ''' + '<br/><br/>' + urls
    #     response.write(html)
    #     return response
    #
    #
    # def post_get(request):
    #     post_id = request.GET.get('post_id')
    #     response = HttpResponse()
    #     html = ''
    #     urls = '''
    #            <br/><br/>
    #            <a href='/blog/post_list/'>list(get or delete) 이동</a><br/>
    #            <a href='/blog/post_create/'>create 이동</a><br/>
    #            '''
    #     try:
    #         post_id = int(post_id)
    #     except ValueError:
    #         print('입력값 에러 :', post_id)
    #         html += '''
    #                 <h3>요청 값 오류</h3>
    #                 ''' + urls
    #         response.write(html)
    #         return response
    #     else:
    #         post = Post.objects.get(id=post_id)
    #         html = f'''
    #                # id: {post.id} <br/>
    #                # user: {post.user.username} <br/>
    #                # title: {post.title} <br/>
    #                # content: {post.content} <br/>
    #                # create_dt: {post.create_dt} <br/>
    #                ''' + urls
    #         response.write(html)
    #         return response
    #
    #
    # @csrf_exempt
    # def post_create(request):
    #     html = '<h3>Post create page</h3><br>'
    #     urls = '''
    #            <br/>
    #            <a href='/blog/post_list/'>list(get or delete) 이동</a><br/>
    #            '''
    #     if request.method == 'GET':
    #         html += '''
    #                 <form action='{% url 'create' %}' method='POST'>
    #                 <input type='hidden' name='username' value='veend'>
    #                 # title : <input type='text' name='title'><br/>
    #                 # content : <br/><input type='textarea' name='content'><br/>
    #                 <input type='submit' value='생성'>
    #                 </form>
    #                 ''' + urls
    #         template = Template(html)
    #         return HttpResponse(template.render(Context()))
    #     if request.method == 'POST':
    #         post = Post()
    #         post.title = request.POST['title']
    #         post.user = User.objects.get_by_natural_key(request.POST['username'])
    #         post.content = request.POST['content']
    #         post.save()
    #         html += '''
    #                 <h4>'포스트 생성 완료'</h4>
    #                 ''' + urls
    #         template = Template(html)
    #         return HttpResponse(template.render(Context()))
    #
    #
    # def post_delete(request):
    #     response = HttpResponse()
    #     html = ''
    #     urls = '''
    #                <br/>
    #                <a href='/blog/post_list/'>list(get or delete) 이동</a><br/>
    #                <a href='/blog/post_create/'>create 이동</a><br/>
    #                '''
    #     post_id = request.GET.get('post_id')
    #
    #     try:
    #         post_id = int(post_id)
    #     except ValueError:
    #         print('입력값 에러 :', post_id)
    #         html += '''
    #                 <h3>요청 값 오류</h3>
    #                 ''' + urls
    #         response.write(html)
    #         return response
    #     else:
    #         post = Post.objects.get(id=post_id)
    #         post.delete()
    #         html += f'<h3># {post_id} 포스트 삭제 완료' + urls
    #         response.write(html)
    #         return response
    #
    #
    #
