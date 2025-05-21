from rest_framework import serializers

from clients.serializers import ClientReadSerializer
from routines.serializers import RoutineSerializer

from .models import Workout


class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workout
        fields = "__all__"
        extra_kwargs = {
            "user": {
                "required": False,
            },
        }
        # depth = 1


class WorkoutReadSerializer(serializers.ModelSerializer):

    client = ClientReadSerializer(read_only=True)
    routines = RoutineSerializer(read_only=True, many=True)

    class Meta:
        model = Workout
        fields = "__all__"
        # depth = 1
