from rest_framework import serializers

from exercises.serializers import ExerciseReadSerializer
from .models import Routine

class RoutineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Routine

        fields = "__all__"

class RoutineReadSerializer(serializers.ModelSerializer):
    exercises = ExerciseReadSerializer(many=True, read_only=True)

    class Meta:
        model = Routine

        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation
