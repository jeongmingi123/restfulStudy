from rest_framework.serializers import ModelSerializer

from .models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'content',
            'created_at',
            'updated_at',
        ]
        read_only_fields = (
            'id',
            'user',
            'created_at',
            'updated_at',
        )
