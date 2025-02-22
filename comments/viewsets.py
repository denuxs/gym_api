from .models import Comment
from .serializers import CommentSerializer

from rest_framework import viewsets


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer