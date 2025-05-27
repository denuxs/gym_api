from measures.models import Measure
from measures.serializers import MeasureReadSerializer
from workouts.models import Workout
from workouts.serializers import WorkoutReadSerializer
from .models import Client
from .serializers import ClientSerializer, ClientReadSerializer

from rest_framework import viewsets, filters
from django_filters.rest_framework import (
    DjangoFilterBackend,
)
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth import get_user_model

User = get_user_model()
from rest_framework.decorators import action


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    search_fields = [
        "user__first_name",
        "user__last_name",
    ]
    filterset_fields = [
        "user",
        "coach",
    ]
    ordering_fields = ["id"]

    def paginate_queryset(self, queryset):
        if "paginator" in self.request.query_params:
            return None
        return super().paginate_queryset(
            queryset,
        )

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return ClientSerializer

        return ClientReadSerializer

    @action(detail=False)
    def workouts(self, request):
        user = request.user
        models = Workout.objects.filter(client=user.client, is_active=True)

        serializer = WorkoutReadSerializer(
            models, many=True, context={"request": request}
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=True)
    def measures(self, request, pk=None):
        # instance = self.get_object()
        models = Measure.objects.filter(client=pk).order_by("-id")

        serializer = MeasureReadSerializer(
            models, many=True, context={"request": request}
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        new_data = self.save_user(data)

        serializer = self.get_serializer(data=new_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        data = request.data.copy()
        instance = self.get_object()

        new_data = self.save_user(data, instance.user)

        serializer = self.get_serializer(instance, data=new_data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def save_user(self, data, user=None):
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        new_password = data.get("password", None)
        is_active = data.get("is_active")

        # TO DO
        bool_map = {"true": True, "false": False}
        is_active = bool_map.get(is_active, False)

        if user:
            user = User.objects.get(id=user.id)
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.is_active = is_active

            if new_password:
                user.set_password(new_password)

            user.save()
        else:
            user = User.objects.create_user(
                username,
                None,
                str(new_password),
                first_name=first_name,
                last_name=last_name,
                is_active=is_active,
            )

        data["user"] = user.id

        data.pop("first_name")
        data.pop("last_name")
        data.pop("username")
        data.pop("is_active")

        if new_password:
            data.pop("password")

        data["coach"] = self.request.user.id

        return data
