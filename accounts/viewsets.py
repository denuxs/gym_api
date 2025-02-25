from .serializers import UserSerializer

# from django.contrib.auth.models import User
from rest_framework.decorators import action

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions

from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterApiView(APIView):

    def post(self, request, format=None):
        user = request.data.copy()

        serializer = UserSerializer(data=user)
        if serializer.is_valid():

            User.objects.create_user(
                user["username"],
                user["email"],
                user["password"],
                first_name=user["first_name"],
                last_name=user["last_name"],
                is_active=user["is_active"],
            )

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
