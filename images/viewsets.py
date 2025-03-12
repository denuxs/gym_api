from .models import Image
from .serializers import ImageSerializer

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["content_type", "object_id"]

    # def get_serializer_class(self):
    #     if self.action in ["create", "update", "partial_update", "destroy"]:
    #         return CommentSerializer

    #     return CommentReadSerializer
