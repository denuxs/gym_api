from .models import Measure
from .serializers import MeasureReadSerializer, MeasureSerializer

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class MeasureViewSet(viewsets.ModelViewSet):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["is_active", "user"]
    search_fields = [
        "user__username",
    ]
    ordering_fields = [
        "id",
    ]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return MeasureSerializer

        return MeasureReadSerializer
