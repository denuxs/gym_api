from rest_framework import serializers

from comments.models import Comment
from comments.serializers import CommentReadSerializer

from .models import Notification

from users.serializers import UserReadSerializer


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

        try:
            comment = Comment.objects.get(id=rep.get("object_id"))
            rep["comment"] = CommentReadSerializer(comment).data
        except Comment.DoesNotExist:
            pass

        return rep
