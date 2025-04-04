from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from workouts.models import Workout
from exercises.models import Exercise
from comments.models import Comment

from django.contrib.auth import get_user_model

User = get_user_model()


class DashboardApiView(APIView):

    def get(self, request, format=None):
        workouts = Workout.objects.count()
        exercises = Exercise.objects.count()
        users = User.objects.count()
        comments = Comment.objects.count()

        data = {
            "workouts": workouts,
            "comments": comments,
            "exercises": exercises,
            "users": users,
        }

        return Response(data)
