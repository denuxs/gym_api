from rest_framework import serializers
from accounts.serializers import UserReadSerializer
from .models import Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = "__all__"


class ClientReadSerializer(serializers.ModelSerializer):
    user = UserReadSerializer(read_only=True)

    class Meta:
        model = Client
        fields = "__all__"
