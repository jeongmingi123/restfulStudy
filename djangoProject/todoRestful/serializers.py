from django.contrib.auth.models import User, Group
from . import models
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TodoRestfulModel
        fields = ['item', 'created']
