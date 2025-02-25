from .models import Exercise
from .serializers import ExerciseReadSerializer, ExerciseSerializer

from rest_framework import viewsets


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return ExerciseSerializer

        return ExerciseReadSerializer
