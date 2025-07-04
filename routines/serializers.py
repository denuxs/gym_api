from rest_framework import serializers

from exercises.serializers import ExerciseReadSerializer
from .models import Routine, RoutineExcercise, UserRoutine


class RoutineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Routine
        fields = "__all__"

    def create(self, validated_data):
        instance = super().create(validated_data)
        exercises = self.initial_data.get("exercises", [])
        # routine = Routine.objects.create(**validated_data)

        for item in exercises:
            RoutineExcercise.objects.create(
                routine=instance,
                exercise_id=item.get("exercise"),
                description=item.get("description"),
                order=item.get("order"),
                sets=item.get("sets"),
            )
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)

        if "exercises" in self.initial_data:
            exercises = self.initial_data.get("exercises")

            instance.exercises.clear()  # Clear existing relationships

            for item in exercises:
                RoutineExcercise.objects.create(
                    routine=instance,
                    exercise_id=item.get("exercise"),
                    description=item.get("description"),
                    order=item.get("order"),
                    sets=item.get("sets"),
                )
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


class UserRoutineSerializer(serializers.ModelSerializer):
    routine = RoutineReadSerializer(read_only=True)
    day = serializers.SerializerMethodField()

    class Meta:
        model = UserRoutine
        fields = "__all__"

    def get_day(self, obj):
        days = {
            1: "Lunes",
            2: "Martes",
            3: "Miércoles",
            4: "Jueves",
            5: "Viernes",
            6: "Sabado",
            7: "Domingo",
        }

        return days[obj.order]
