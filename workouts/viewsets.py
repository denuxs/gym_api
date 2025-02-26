from .models import Workout
from .serializers import WorkoutSerializer, WorkoutReadSerializer

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "user",
    ]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return WorkoutSerializer

        return WorkoutReadSerializer
