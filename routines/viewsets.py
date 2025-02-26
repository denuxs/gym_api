from .models import Routine
from .serializers import RoutineSerializer, RoutineReadSerializer

from rest_framework import viewsets


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return RoutineSerializer

        return RoutineReadSerializer

