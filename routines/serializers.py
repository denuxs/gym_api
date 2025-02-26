from rest_framework import serializers

from exercises.serializers import ExerciseSerializer
from .models import Routine

class RoutineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Routine

        fields = "__all__"

class RoutineReadSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = Routine

        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation
