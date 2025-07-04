from .models import Notification
from .serializers import NotificationSerializer, NotificationReadSerializer

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_fields = ["user", "user_to", "is_read"]
    ordering_fields = [
        "id",
    ]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return NotificationSerializer

        return NotificationReadSerializer
