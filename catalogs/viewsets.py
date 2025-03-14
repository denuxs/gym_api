from .models import Catalog, Muscle
from .serializers import CatalogSerializer, MuscleSerializer

from rest_framework import viewsets


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer


class MuscleViewSet(viewsets.ModelViewSet):
    queryset = Muscle.objects.all()
    serializer_class = MuscleSerializer
