from accounts.models import Fcmtoken
from .serializers import FcmTokenSerializer, UserReadSerializer, UserSerializer

# from django.contrib.auth.models import User
from rest_framework.decorators import action

from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterApiView(APIView):

    def post(self, request, format=None):
        user = request.data.copy()
        # email = f"{user["username"]}@local.com"

        serializer = UserSerializer(data=user)
        if serializer.is_valid():

            User.objects.create_user(
                user["username"],
                None,
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

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = ["is_active", "is_superuser"]
    search_fields = [
        "username",
    ]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return UserSerializer

        return UserReadSerializer

    def update(self, request, *args, **kwargs):
        data = request.data.copy()
        instance = self.get_object()

        if "password" in data:
            password = request.data.get("password")
            instance.set_password(password)
            data.pop("password")

        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    @action(detail=False)
    def me(self, request):
        serializer = UserReadSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class FcmTokenViewSet(viewsets.ModelViewSet):
    queryset = Fcmtoken.objects.all()
    serializer_class = FcmTokenSerializer

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "user",
    ]
