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
    # search_fields = [
    #     "client__username",
    # ]
    ordering_fields = [
        "id",
    ]

    def paginate_queryset(self, queryset):
        if "paginator" in self.request.query_params:
            return None
        return super().paginate_queryset(
            queryset,
        )

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return MeasureSerializer

        return MeasureReadSerializer
