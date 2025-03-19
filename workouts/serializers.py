from rest_framework import serializers

from accounts.serializers import UserSerializer
from exercises.serializers import ExerciseReadSerializer

from .models import Workout, WorkoutExcercise


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = "__all__"


class WorkoutExcerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseReadSerializer(read_only=True)

    class Meta:
        model = WorkoutExcercise
        fields = "__all__"


class WorkoutReadSerializer(serializers.ModelSerializer):
    # day = serializers.CharField(source="get_day_display")
    exercises = WorkoutExcerciseSerializer(
        many=True, read_only=True, source="workoutexcercise_set"
    )

    # routines_name = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Workout
        fields = "__all__"
        # depth = 1

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     return representation

    # def get_routines_name(self, obj):
    #     data = []
    #     for item in obj.routines.all():
    #         data.append(item.name)

    #     return data
