from .models import Image
from .serializers import ImageSerializer

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_fields = ["content_type", "object_id"]

    ordering_fields = [
        "id",
    ]

    def paginate_queryset(self, queryset):
        if "paginator" in self.request.query_params:
            return None
        return super().paginate_queryset(
            queryset,
        )
