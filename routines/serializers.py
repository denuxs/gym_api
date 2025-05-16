from rest_framework import serializers

from exercises.serializers import ExerciseReadSerializer
from .models import Routine, RoutineExcercise


class RoutineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Routine

        fields = "__all__"

    def update(self, instance, validated_data):
        if "exercises" in self.initial_data:
            exercises = self.initial_data.get("exercises")

            # print(instance.exercises.all())

            for item in exercises:
                id = item.get("id")

                if not id:
                    RoutineExcercise.objects.create(
                        workout_id=item.get("workout"),
                        exercise_id=item.get("exercise"),
                        description=item.get("description"),
                        order=item.get("order"),
                        data=item.get("sets"),
                    )
                    continue

                find = RoutineExcercise.objects.get(pk=id)
                if find:
                    find.workout_id = item.get("workout")
                    find.exercise_id = item.get("exercise")
                    find.description = item.get("description")
                    find.order = item.get("order")
                    find.data = item.get("sets")
                    find.save()

        # instance.workoutexcercise_set.set(details)
        instance.__dict__.update(**validated_data)
        instance.save()
        return instance


class RoutineExcerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseReadSerializer(read_only=True)

    class Meta:
        model = RoutineExcercise
        fields = "__all__"


class RoutineReadSerializer(serializers.ModelSerializer):
    level_display = serializers.CharField(source="get_level_display", read_only=True)
    # exercises = ExerciseReadSerializer(many=True, read_only=True)

    exercises = RoutineExcerciseSerializer(
        many=True, read_only=True, source="routineexcercise_set"
    )

    class Meta:
        model = Routine

        fields = "__all__"

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     return representation
