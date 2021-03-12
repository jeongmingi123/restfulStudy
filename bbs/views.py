from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

import json

from .models import Post

# Create your views here.

# By using ViewSet /  Django Rest API Framework
'''
from rest_framework import viewsets
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
'''

# 함수 기반 View
def ListData(request):
    
    # 데이터베이스에서 데이터 가져오기
    posts = Post.objects.all().order_by('date')[::-1]

    # Django 객체를 Json 데이터로 변환
    toJson = serializers.serialize('json', posts, 
                fields=['title', 'author', 'content', 'date'])

    return HttpResponse(toJson, status=200, content_type='application/json', charset='utf-8')


def DetailData(request, key):
    
    # 데이터베이스에서 데이터 가져오기
    posts = Post.objects.filter(pk=key)

    # Django 객체를 Json 데이터로 변환
    toJson = serializers.serialize('json', posts, 
                fields=['title', 'author', 'content', 'date'])
    return HttpResponse(toJson, status=200, content_type='application/json', charset='utf-8')
    

@csrf_exempt
def PostData(request):

    # Json 형태의 요청을 받은 경우
    if request.META['CONTENT_TYPE'] == 'application/json':
        
        # json.loads ; Json 형태의 String을 Python Dict 형태로 변환
        # Body를 통해 접근
        request = json.loads(request.body)
        newPost = Post(
            title=request['title'],
            author=request['author'],
            content=request['content'],
            )
    
    # Form-data 또는 x-www-urlencoded 형태의 요청을 받은 경우
    else:
        newPost = Post(
            title=request.POST['title'],
            author=request.POST['author'],
            content=request.POST['content'],
            )
    newPost.save()
        
    return HttpResponse(status=200)


@csrf_exempt
def DeleteData(request):

    # Json 형태의 요청을 받은 경우
    if request.META['CONTENT_TYPE'] == 'application/json':
        request = json.loads(request.body)
        key = request['pk']

    # Form-data 또는 x-www-urlencoded 형태의 요청을 받은 경우
    else:
        request = request.body.decode('utf-8').split('&')
        request = {i[0]: i[1] for req in request if (i := req.split('='))}
        key = request['pk']
    
    targetPost = Post.objects.get(pk=key)
    targetPost.delete()

    return HttpResponse(status=200)