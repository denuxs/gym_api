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
        email = f"{user["username"]}@local.com"

        serializer = UserSerializer(data=user)
        if serializer.is_valid():

            User.objects.create_user(
                user["username"],
                email,
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

    def create(self, request, *args, **kwargs):
        user = request.data.copy()        
        email = f"{user["username"]}@local.com"

        serializer = self.get_serializer(data=user)
        serializer.is_valid(raise_exception=True)

        User.objects.create_user(
            user["username"],
            email,
            user["password"],
            first_name=user["first_name"],
            last_name=user["last_name"],
            is_active=user["is_active"],
        )

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
    
    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     return Response(serializer.data)
