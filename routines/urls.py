from rest_framework.routers import DefaultRouter
from .viewsets import (
    RoutineExerciseViewSet,
    RoutineViewSet,
)

router = DefaultRouter()
router.register("routines", RoutineViewSet)
router.register("routineexercises", RoutineExerciseViewSet)

urlpatterns = router.urls
