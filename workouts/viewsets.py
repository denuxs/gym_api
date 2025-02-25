from .models import Workout
from .serializers import WorkoutSerializer

from rest_framework import viewsets


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
