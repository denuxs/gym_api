from .models import Comment, CommentReplies
from .serializers import (
    CommentRepliesSerializer,
    CommentSerializer,
    CommentReadSerializer,
)

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ["user", "object_id", "content_type"]
    ordering_fields = [
        "id",
    ]
    search_fields = [
        "user__username",
    ]
    # ordering = ["-id"]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return CommentSerializer

        return CommentReadSerializer


class CommentRepliesViewSet(viewsets.ModelViewSet):
    queryset = CommentReplies.objects.all()
    serializer_class = CommentRepliesSerializer
