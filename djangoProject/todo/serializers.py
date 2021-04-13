from . import models
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Todo
        fields = ['date', 'item']
