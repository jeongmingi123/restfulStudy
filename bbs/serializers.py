from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post                                            # 모델 설정
        fields = ('id', 'title', 'author', 'content', 'date')   # 필드 설정
