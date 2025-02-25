from .models import Comment
from .serializers import CommentSerializer, CommentReadSerializer

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user", "object_id"]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return CommentSerializer

        return CommentReadSerializer
