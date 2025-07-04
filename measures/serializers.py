from rest_framework import serializers

from .models import Measure


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = "__all__"


class MeasureReadSerializer(serializers.ModelSerializer):

    fullname = serializers.CharField(source="user.get_full_name")

    class Meta:
        model = Measure
        fields = "__all__"
