from rest_framework import serializers

from catalogs.models import Muscle

class MuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle
        fields = "__all__"