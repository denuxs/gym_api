from .models import Notification
from .serializers import NotificationSerializer

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "user",
    ]
    ordering_fields = [
        "id",
    ]
