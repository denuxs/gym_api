from .models import Equipment
from .serializers import EquipmentSerializer

from rest_framework import viewsets


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer