from rest_framework import viewsets
from .serializers import StudyBoardSerializer
from .models import Post


class StudyBoardViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = StudyBoardSerializer
