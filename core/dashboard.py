from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView

from routines.models import Routine
from exercises.models import Exercise

from django.contrib.auth import get_user_model

User = get_user_model()


class DashboardApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        routines = Routine.objects.count()
        exercises = Exercise.objects.count()
        clients = User.objects.filter(role="client").count()
        coaches = User.objects.filter(role="coach").count()

        data = {
            "routines": routines,
            "exercises": exercises,
            "clients": clients,
            "coaches": coaches,
        }

        return Response(data)
