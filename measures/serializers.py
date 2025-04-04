from rest_framework import serializers

from accounts.serializers import UserSerializer

from .models import Measure

class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = "__all__"
class MeasureReadSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Measure
        fields = "__all__"