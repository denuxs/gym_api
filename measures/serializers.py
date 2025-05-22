from rest_framework import serializers

from clients.serializers import ClientSerializer

from .models import Measure


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = "__all__"


class MeasureReadSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)

    class Meta:
        model = Measure
        fields = "__all__"
