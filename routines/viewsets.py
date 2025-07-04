from .models import Routine, RoutineExcercise, UserRoutine
from .serializers import (
    RoutineExcerciseSerializer,
    RoutineSerializer,
    RoutineReadSerializer,
    UserRoutineSerializer,
)

from rest_framework import viewsets, filters
from django_filters.rest_framework import (
    DjangoFilterBackend,
)


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = [
        "title",
    ]
    filterset_fields = [
        "level",
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
            return RoutineSerializer

        return RoutineReadSerializer


class RoutineExerciseViewSet(viewsets.ModelViewSet):
    queryset = RoutineExcercise.objects.all()
    serializer_class = RoutineExcerciseSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = [
        "order",
    ]

    # def get_serializer_class(self):
    #     if self.action in ["create", "update", "partial_update", "destroy"]:
    #         return RoutineSerializer

    #     return RoutineReadSerializer


class UserRoutineViewSet(viewsets.ModelViewSet):
    queryset = UserRoutine.objects.all()
    serializer_class = UserRoutineSerializer
