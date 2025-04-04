from rest_framework import serializers

from catalogs.serializers import CatalogSerializer
from .models import Exercise


class ExerciseReadSerializer(serializers.ModelSerializer):
    equipment = CatalogSerializer(read_only=True)
    muscle = CatalogSerializer(read_only=True)

    class Meta:
        model = Exercise
        fields = "__all__"


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"
