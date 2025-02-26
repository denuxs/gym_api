from rest_framework import serializers

from accounts.serializers import UserSerializer
from routines.serializers import RoutineSerializer

from .models import Workout


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = "__all__"


class WorkoutReadSerializer(serializers.ModelSerializer):
    # day = serializers.CharField(source="get_day_display")
    routines = RoutineSerializer(many=True, read_only=True)

    routines_name = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Workout
        fields = "__all__"

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     return representation

    def get_routines_name(self, obj):
        data = []
        for item in obj.routines.all():
            data.append(item.name)

        return data
