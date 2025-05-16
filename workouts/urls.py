from rest_framework.routers import DefaultRouter
from .viewsets import (
    WorkoutViewSet,
)

router = DefaultRouter()
router.register("workouts", WorkoutViewSet)

urlpatterns = router.urls
