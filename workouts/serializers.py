from rest_framework import serializers

from routines.serializers import RoutineSerializer

from .models import Workout


class WorkoutSerializer(serializers.ModelSerializer):

    # routines = RoutineSerializer(many=True, read_only=True)
    routines = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # routines = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='name'
    #  )
    
    class Meta:
        model = Workout
        fields = "__all__"


