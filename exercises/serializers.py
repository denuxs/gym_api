from rest_framework import serializers

from users.serializers import UserSerializer
from catalogs.serializers import CatalogSerializer
from .models import Exercise


class ExerciseReadSerializer(serializers.ModelSerializer):
    equipment = CatalogSerializer(read_only=True)
    muscle = CatalogSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Exercise
        fields = "__all__"


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"
        extra_kwargs = {
            "user": {
                "required": False,
            },
        }
