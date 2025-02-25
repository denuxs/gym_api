from .models import Measure
from .serializers import MeasureSerializer

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class MeasureViewSet(viewsets.ModelViewSet):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']