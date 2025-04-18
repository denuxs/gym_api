from .models import Workout, WorkoutExcercise
from .serializers import (
    WorkoutExcerciseSerializer,
    WorkoutSerializer,
    WorkoutReadSerializer,
)

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
    filterset_fields = ["user", "day", "is_active"]
    ordering_fields = [
        "day",
    ]
    ordering = ["-id"]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return WorkoutSerializer

        return WorkoutReadSerializer


class WorkoutDetailViewSet(viewsets.ModelViewSet):
    queryset = WorkoutExcercise.objects.all()
    serializer_class = WorkoutExcerciseSerializer
