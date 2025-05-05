from .models import Exercise
from .serializers import ExerciseReadSerializer, ExerciseSerializer

from rest_framework import viewsets, filters
from django_filters.rest_framework import (
    DjangoFilterBackend,
)
from rest_framework.decorators import action
from rest_framework.response import Response

from comments.models import Comment
from comments.serializers import CommentReadSerializer
from django.contrib.contenttypes.models import ContentType


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        "name",
    ]
    filterset_fields = [
        "muscle",
        "equipment",
    ]
    ordering_fields = ["id", "name", "muscle", "equipment"]

    def paginate_queryset(self, queryset):
        if "paginator" in self.request.query_params:
            return None
        return super().paginate_queryset(
            queryset,
        )

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return ExerciseSerializer

        return ExerciseReadSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(["GET"], detail=True, url_path="comments")
    def comments(self, request, pk):
        exercise = self.get_object()
        content = ContentType.objects.get_for_model(Exercise)

        comment = Comment.objects.filter(
            object_id=exercise.id,
            content_type=content,
        )

        serializer = CommentReadSerializer(
            comment, many=True, context={"request": request}
        )

        return Response(serializer.data)
