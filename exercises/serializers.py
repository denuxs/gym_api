from rest_framework import serializers

from catalogs.serializers import CatalogSerializer

# from catalogs.serializers import MuscleSerializer

from .models import Exercise

# from equipments.serializers import EquipmentSerializer
from comments.serializers import CommentReadSerializer, CommentSerializer


class ExerciseReadSerializer(serializers.ModelSerializer):
    equipment = CatalogSerializer(read_only=True)
    muscle = CatalogSerializer(read_only=True)

    # comments = CommentReadSerializer(many=True, read_only=True)

    class Meta:
        model = Exercise
        fields = "__all__"


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"
