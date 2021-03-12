from django.shortcuts import render, redirect
from . import models


def all_blog(request):
    all_blogs = models.Blog.objects.all()
    return render(request, "all_views.html", context={"blogs": all_blogs})


def bloging(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    blog = models.Blog.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'bloging.html', context={'blog': blog})


def new_blog(request):

    if request.method == 'POST':
        new_article = models.Blog.objects.create(
            title=request.POST['title'],
            text=request.POST['text'],
            comment=request.POST['comment'],
        )
        return redirect('/blog/')
    return render(request, 'new_blog.html')
