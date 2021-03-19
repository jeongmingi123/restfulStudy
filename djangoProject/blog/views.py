from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.views import View

# View 만 이용해서 사용
class All_blog(View):

    def get(self, request):
        all_blogs = models.Blog.objects.all()
        return render(request, "all_views.html", context={"blogs": all_blogs})


class Bloging(View):

    def get(self, request, pk):
        blog = models.Blog.objects.get(pk=pk)
        return render(request, 'bloging.html', context={'blog': blog})


class New_blog(View):

    def get(self, request):
        return render(request, 'new_blog.html')

    def post(self, request):
        new_blog = models.Blog.objects.create(
            title=request.POST['title'],
            text=request.POST['text'],
            comment=request.POST['comment'],
        )
        return redirect('/blog/')


class Remove_blog(View):

    def get(self, request, pk):
        blog = models.Blog.objects.get(pk=pk)
        blog.delete()
        return redirect('/blog/')


class Edit_blog(View):

    def get(self, request, pk):
        blog = models.Blog.objects.get(pk=pk)
        return render(request, 'edit_blog.html', {'blog': blog})

    def post(self, request, pk):
        blog = models.Blog.objects.get(pk=pk)
        blog.title = request.POST['title']
        blog.text = request.POST['text']
        blog.comment = request.POST['comment']
        blog.save()
        return redirect(f'/blog/{blog.pk}')



# 이전 FBV 내용

# # 모든 블로그 글 내용 메소드
# def all_blog(request):
#
#     all_blogs = models.Blog.objects.all()
#
#     # context 첫번째 인자는 html 템플릿에 보낼 변수이름, 두번째는 함수에서 보낼 변수
#     return render(request, "all_views.html", context={"blogs": all_blogs})
#
#
# # 블로그 개인 작성이 작성한 내용을 보여주는 메소드
# def bloging(request, pk):
#     # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
#     blog = models.Blog.objects.get(pk=pk)
#
#     # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
#     return render(request, 'bloging.html', context={'blog': blog})
#
#
# # 새로운 블로그 글 생성하는 메소드
# def new_blog(request):
#     if request.method == 'POST': # 요청된 방법이 POST 방식이면, create 메소드 사용하여, DB 생성
#         new_blog = models.Blog.objects.create(
#             title = request.POST['title'],
#             text = request.POST['text'],
#             comment = request.POST['comment'],
#         )
#         return redirect('/blog/')
#     return render(request, 'new_blog.html')
#
#
# # 블로그 글 지우는 메소드
# def remove_blog(request, pk):
#
#     blog = models.Blog.objects.get(pk=pk)
#
#     if request.method == 'POST':
#         blog.delete()
#         return redirect('/blog/')
#     return render(request, 'remove_blog.html', {'blog': blog})
#
#
# # 블로그 글 수정하는 메소드
# def edit_blog(requset, pk):
#     blog = models.Blog.objects.get(pk=pk)
#     if requset.method == 'POST':
#         blog.title = requset.POST['title']
#         blog.text = requset.POST['text']
#         blog.comment = requset.POST['comment']
#         blog.save()
#         return redirect(f'/blog/{blog.pk}')
#     return render(request, 'edit_blog.html', {'blog': blog})
