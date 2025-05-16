from .models import Routine
from .serializers import RoutineSerializer, RoutineReadSerializer

from rest_framework import viewsets, filters
from django_filters.rest_framework import (
    DjangoFilterBackend,
)


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        "title",
    ]
    filterset_fields = [
        "level",
    ]
    ordering_fields = [
        "id",
    ]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return RoutineSerializer

        return RoutineReadSerializer
