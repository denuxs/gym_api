from rest_framework import serializers

from comments.models import Comment
from comments.serializers import CommentSerializer

from .models import Notification
from accounts.serializers import UserReadSerializer


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = "__all__"


class NotificationReadSerializer(serializers.ModelSerializer):
    user = UserReadSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        comment = Comment.objects.get(id=rep.get("object_id"))
        rep["comment"] = CommentSerializer(comment).data
        return rep
