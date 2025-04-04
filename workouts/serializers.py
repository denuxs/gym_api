from rest_framework import serializers

from accounts.serializers import UserSerializer
from exercises.serializers import ExerciseReadSerializer

from .models import Workout, WorkoutExcercise


class WorkoutExcerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseReadSerializer(read_only=True)

    class Meta:
        model = WorkoutExcercise
        fields = "__all__"


class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workout
        fields = "__all__"
        # depth = 1

    # def create(self, validated_data):
    #     workout = Workout.objects.create(**validated_data)
    #     if "exercises" in self.initial_data:
    #         exercises = self.initial_data.get("exercises")
    #         for exercise in exercises:
    #             WorkoutExcercise.objects.create(
    #                 workout=workout,
    #                 exercise_id=exercise.get("exercise"),
    #                 repts=exercise.get("repts"),
    #                 sets=exercise.get("sets"),
    #                 weight=exercise.get("weight"),
    #             )
    #     return workout

    # @transaction.atomic
    def update(self, instance, validated_data):
        if "exercises" in self.initial_data:
            exercises = self.initial_data.get("exercises")
            # print(instance.exercises.all())

            for item in exercises:
                exercise, created = WorkoutExcercise.objects.update_or_create(
                    pk=item.get("id"),
                    workout_id=item.get("workout"),
                    exercise_id=item.get("exercise"),
                    description=item.get("description"),
                    repts=item.get("repts"),
                    sets=item.get("sets"),
                    weight=item.get("weight"),
                )
        # instance.workoutexcercise_set.set(details)
        instance.__dict__.update(**validated_data)
        instance.save()
        return instance


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
        depth = 1

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     return representation

    # def get_routines_name(self, obj):
    #     data = []
    #     for item in obj.routines.all():
    #         data.append(item.name)

    #     return data
