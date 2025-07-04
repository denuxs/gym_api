from rest_framework import serializers

from exercises.models import Exercise
from exercises.serializers import ExerciseSerializer

from .models import Comment, CommentReplies

from users.serializers import UserReadSerializer


class CommentRepliesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentReplies
        fields = "__all__"


class CommentReadSerializer(serializers.ModelSerializer):
    user = UserReadSerializer(read_only=True)
    replies = CommentRepliesSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        # depth = 1
        fields = "__all__"

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)

    #     exercise = Exercise.objects.get(id=rep.get("object_id"))
    #     rep["exercise"] = ExerciseSerializer(exercise).data
    #     return rep


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)

    #     exercise = Exercise.objects.get(id=rep.get("object_id"))
    #     rep["exercise"] = ExerciseSerializer(exercise).data
    #     return rep
