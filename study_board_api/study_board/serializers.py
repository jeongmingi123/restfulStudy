from rest_framework import serializers
from .models import Post


class StudyBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'user', 'content', 'create_dt', 'modify_dt')
