from django.shortcuts import render, redirect
from . import models


def all_blog(request):  # 모든 블로그 내용
    all_blogs = models.Blog.objects.all()
    return render(request, "all_views.html", context={"blogs": all_blogs})


def bloging(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    blog = models.Blog.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'bloging.html', context={'blog': blog})


def new_blog(request):  # 요청된 방법이 POST 방식이면, create 메소드 사용하여, DB 생성

    if request.method == 'POST':
        new_blog = models.Blog.objects.create(
            title=request.POST['title'],
            text=request.POST['text'],
            comment=request.POST['comment'],
        )
        return redirect('/blog/')
    return render(request, 'new_blog.html')


def remove_blog(request, pk):

    blog = models.Blog.objects.get(pk=pk)

    if request.method == 'POST':
        blog.delete()
        return redirect('/blog/')
    return render(request, 'remove_blog.html', {'blog': blog})
