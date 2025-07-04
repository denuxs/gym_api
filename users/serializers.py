from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from rest_framework_simplejwt.tokens import Token

# from accounts.models import Fcmtoken

from flags.models import FlagState
from django.contrib.contenttypes.models import ContentType
import json
from django.contrib.auth import get_user_model

from routines.models import UserRoutine

User = get_user_model()


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = "__all__"


class FlagStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlagState
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "is_staff",
            "password",
            "is_active",
            "company",
            "avatar",
            "role",
            "coach",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        new_password = validated_data.pop("password", None)
        user = User(**validated_data)

        if new_password:
            user.set_password(new_password)

        user.save()

        if "routines" in self.initial_data:
            routines_str = self.initial_data.get("routines", [])
            routines = json.loads(routines_str)

            for item in routines:
                UserRoutine.objects.create(
                    user=user,
                    routine_id=item.get("routine"),
                    order=item.get("order"),
                )

        return user

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)

        if "routines" in self.initial_data:
            routines_str = self.initial_data.get("routines")
            routines = json.loads(routines_str)

            # Clear existing relationships
            UserRoutine.objects.filter(user=instance).delete()

            for item in routines:
                UserRoutine.objects.create(
                    user=instance,
                    routine_id=item.get("routine"),
                    order=item.get("order"),
                )
        return instance


class UserReadSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="get_full_name")
    fullname = serializers.CharField(source="get_full_name")

    role_display = serializers.CharField(source="get_role_display", read_only=True)

    class Meta:
        model = User
        exclude = ["password"]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data["user"] = UserReadSerializer(self.user).data
        return data


# class FcmTokenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Fcmtoken
#         fields = "__all__"

#     def create(self, validated_data):
#         token = validated_data.get("token")
#         if token:
#             model = Fcmtoken.objects.filter(token=token).first()

#             if not model:
#                 return Fcmtoken.objects.create(**validated_data)

#             return model
