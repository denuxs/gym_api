from rest_framework import serializers

from users.serializers import UserReadSerializer
from .models import Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = "__all__"


class ClientReadSerializer(serializers.ModelSerializer):
    coach = UserReadSerializer(read_only=True)
    username = serializers.CharField(source="user.username")
    fullname = serializers.CharField(source="user.get_full_name")
    user = UserReadSerializer(read_only=True)

    class Meta:
        model = Client
        fields = "__all__"
        # extra_kwargs = {
        #     "coach": {
        #         "required": False,
        #     },
        # }
