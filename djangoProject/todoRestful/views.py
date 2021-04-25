from django.contrib.auth.models import User, Group
from .serializers import TodoSerializer
from rest_framework import viewsets, status
from .models import TodoRestfulModel

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.shortcuts import get_object_or_404


# class TodoViewSet(viewsets.ModelViewSet):
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAdminUser]
#
#     def get(self, request):
#         serializer = TodoSerializer(TodoRestfulModel.objects.all(), many=True)
#
#     def post(self, request):
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


class TodoListAPIView(APIView):
    def get(self, request):
        serializer = TodoSerializer(TodoRestfulModel.objects.all(), many=True)
        return Response(serializer.data, status=201)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# 포스팅 내용, 수정, 삭제
class TodoDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(TodoRestfulModel, pk=pk)

    def get(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
