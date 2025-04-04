from rest_framework import serializers

from django.contrib.auth import get_user_model

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
