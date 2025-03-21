from rest_framework.decorators import action
from .models import Workout
from .serializers import WorkoutSerializer, WorkoutReadSerializer
from rest_framework.response import Response

from rest_framework import viewsets, filters
from django_filters.rest_framework import (
    DjangoFilterBackend,
)


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        "user__username",
    ]
    filterset_fields = ["user", "day"]
    ordering_fields = [
        "day",
    ]
    ordering = ["-id"]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return WorkoutSerializer

        return WorkoutReadSerializer

    # @action(detail=True, methods=['get'])
    # def items_not_done(self, request):
    #     user_count = Item.objects.filter(done=False).count()

    #     return Response(user_count)
