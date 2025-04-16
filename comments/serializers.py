from rest_framework import serializers

from exercises.models import Exercise
from exercises.serializers import ExerciseSerializer

from .models import Comment
from accounts.serializers import UserReadSerializer


class CommentReadSerializer(serializers.ModelSerializer):
    user = UserReadSerializer()

    class Meta:
        model = Comment
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        exercise = Exercise.objects.get(id=rep.get("object_id"))
        rep["exercise"] = ExerciseSerializer(exercise).data
        return rep


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)

    #     exercise = Exercise.objects.get(id=rep.get("object_id"))
    #     rep["exercise"] = ExerciseSerializer(exercise).data
    #     return rep
