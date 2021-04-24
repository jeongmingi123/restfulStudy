from django.contrib.auth.models import User, Group
from .serializers import TodoSerializer
from rest_framework import viewsets
from rest_framework import permissions
from .models import TodoRestfulModel


class TodoViewSet(viewsets.ModelViewSet):

    queryset = TodoRestfulModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
