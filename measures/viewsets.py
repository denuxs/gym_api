from .models import Measure
from .serializers import MeasureSerializer

from rest_framework import viewsets


class MeasureViewSet(viewsets.ModelViewSet):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer