from rest_framework import serializers

from routines.serializers import RoutineSerializer

from .models import Workout


class WorkoutSerializer(serializers.ModelSerializer):
    day = serializers.CharField(source='get_day_display')

    routines = RoutineSerializer(many=True, read_only=True)
    # routines = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # routines_name = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='name'
    #  )

    routines_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Workout
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['routines_count'] = instance.routines.count()

        return representation

    def get_routines_name(self, obj):

        data = []
        for item in obj.routines.all():
            data.append(item.name)

        return data


