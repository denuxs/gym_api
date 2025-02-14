from rest_framework import serializers

from catalogs.serializers import MuscleSerializer

from .models import Exercise
from equipments.serializers import EquipmentSerializer


class ExerciseSerializer(serializers.ModelSerializer):
    equipment = EquipmentSerializer(read_only=True)
    muscle = MuscleSerializer(read_only=True)
    class Meta:
        model = Exercise
        fields = "__all__"
