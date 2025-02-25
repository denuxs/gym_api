from .models import Muscle
from .serializers import MuscleSerializer

from rest_framework import viewsets


class MuscleViewSet(viewsets.ModelViewSet):
    queryset = Muscle.objects.all()
    serializer_class = MuscleSerializer
