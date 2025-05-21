from .models import Workout
from .serializers import (
    WorkoutSerializer,
    WorkoutReadSerializer,
)

from rest_framework import viewsets, filters
from django_filters.rest_framework import (
    DjangoFilterBackend,
)
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    # permission_classes = [IsAuthenticated, IsAdmin]

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    # search_fields = [
    #     "user__username",
    # ]
    filterset_fields = ["user", "client", "is_active"]
    # ordering_fields = [
    #     "day",
    # ]
    # ordering = ["-id"]

    def paginate_queryset(self, queryset):
        if "paginator" in self.request.query_params:
            return None
        return super().paginate_queryset(
            queryset,
        )

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return WorkoutSerializer

        return WorkoutReadSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


# class WorkoutDetailViewSet(viewsets.ModelViewSet):
#     queryset = WorkoutExcercise.objects.all()
#     serializer_class = WorkoutExcerciseSerializer
