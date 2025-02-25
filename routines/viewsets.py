from .models import Routine
from .serializers import RoutineSerializer

from rest_framework import viewsets


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
