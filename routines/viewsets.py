from .models import Routine
from .serializers import RoutineSerializer

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['user']