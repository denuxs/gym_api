from rest_framework import serializers

from exercises.serializers import ExerciseSerializer
from .models import Routine

# class RoutineDetailSerializer(serializers.ModelSerializer):
#     exercise = ExerciseSerializer(read_only=True)
#     class Meta:
#         model = RoutineDetail

#         fields = "__all__"

class RoutineSerializer(serializers.ModelSerializer):
    # exercises = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='name'
    #  )
    # exercises = RoutineDetailSerializer(source="routinedetail_set", many=True, read_only=True)
    exercises = ExerciseSerializer(many=True)
    class Meta:
        model = Routine

        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['exercises_count'] = instance.exercises.count()

        return representation
