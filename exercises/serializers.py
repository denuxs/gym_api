from rest_framework import serializers

from catalogs.serializers import MuscleSerializer

from .models import Exercise
from equipments.serializers import EquipmentSerializer
from comments.serializers import CommentSerializer


class ExerciseReadSerializer(serializers.ModelSerializer):
    equipment = EquipmentSerializer(read_only=True)
    muscle = MuscleSerializer(read_only=True)

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Exercise
        fields = "__all__"


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"
