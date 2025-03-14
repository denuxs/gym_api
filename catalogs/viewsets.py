from .models import Catalog, Muscle
from .serializers import CatalogSerializer, MuscleSerializer

from rest_framework import viewsets, filters
from django_filters.rest_framework import (
    DjangoFilterBackend,
)

class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    # search_fields = [
    #     "user__username",
    # ]
    filterset_fields = ["key",]
    ordering_fields = [
        "key", "name"
    ]
    # ordering = ["-id"]


class MuscleViewSet(viewsets.ModelViewSet):
    queryset = Muscle.objects.all()
    serializer_class = MuscleSerializer
