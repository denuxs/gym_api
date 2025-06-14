from clients.models import Client
from clients.serializers import ClientReadSerializer
from workouts.models import Workout
from workouts.serializers import WorkoutReadSerializer
from .serializers import UserReadSerializer, UserSerializer
from rest_framework.decorators import action
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from flags.models import FlagState
from .serializers import FlagStateSerializer, ContentTypeSerializer
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth import get_user_model

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    search_fields = [
        "username",
        "first_name",
        "last_name",
    ]
    ordering_fields = [
        "id",
    ]

    def paginate_queryset(self, queryset):
        if "paginator" in self.request.query_params:
            return None
        return super().paginate_queryset(
            queryset,
        )

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return UserSerializer

        return UserReadSerializer

    def update(self, request, *args, **kwargs):
        data = request.data.copy()
        instance = self.get_object()

        if "password" in data:
            password = data.get("password")
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

    @action(detail=False)
    def clients(self, request):
        user = request.user
        models = Client.objects.filter(coach=user)

        serializer = ClientReadSerializer(
            models, many=True, context={"request": request}
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False)
    def workouts(self, request):
        user = request.user
        models = Workout.objects.filter(user=user, is_active=True)

        serializer = WorkoutReadSerializer(
            models, many=True, context={"request": request}
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False)
    def flags(self, request):
        models = FlagState.objects.all()
        serializer = FlagStateSerializer(
            models, many=True, context={"request": request}
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False)
    def contenttypes(self, request):
        models = ContentType.objects.all()
        serializer = ContentTypeSerializer(
            models, many=True, context={"request": request}
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)
