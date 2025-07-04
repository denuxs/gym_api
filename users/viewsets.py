from measures.models import Measure
from measures.serializers import MeasureSerializer
from routines.models import UserRoutine
from routines.serializers import UserRoutineSerializer

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
    filterset_fields = ["is_active", "is_staff", "is_superuser", "role", "coach"]
    # filterset_fields = {
    #     'role': ["in", "exact"],
    #     'is_active': ["exact"],
    #     'is_staff': ["exact"],
    #     'is_superuser': ["exact"]
    # }
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

    @action(detail=True)
    def routines(self, request, pk=None):
        # instance = self.get_object()
        models = UserRoutine.objects.filter(user=pk).order_by("order")

        serializer = UserRoutineSerializer(
            models, many=True, context={"request": request}
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=True)
    def measures(self, request, pk=None):
        models = Measure.objects.filter(user=pk).order_by("-id")

        serializer = MeasureSerializer(models, many=True, context={"request": request})
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
