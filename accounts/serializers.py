from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token

from django.contrib.auth import get_user_model
from accounts.models import Fcmtoken

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        fields = [
            "id",
            "username",
            "photo",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "phone",
            "age",
            "gender",
            "password",
        ]

    def create(self, validated_data):
        new_password = validated_data.pop("password", None)
        user = User(**validated_data)

        if new_password:
            user.set_password(new_password)

        user.save()
        return user


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data["user"] = UserReadSerializer(self.user).data
        return data


class FcmTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fcmtoken
        fields = "__all__"

    def create(self, validated_data):
        token = validated_data.get("token")
        if token:
            model = Fcmtoken.objects.filter(token=token).first()

            if not model:
                return Fcmtoken.objects.create(**validated_data)

            return model
