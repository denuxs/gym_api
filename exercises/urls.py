from rest_framework.routers import DefaultRouter
from .viewsets import (
    ExerciseViewSet,
)

router = DefaultRouter()
router.register("exercises", ExerciseViewSet)

urlpatterns = router.urls
