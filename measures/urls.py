from rest_framework.routers import DefaultRouter
from .viewsets import (
    MeasureViewSet,
)

router = DefaultRouter()
router.register("measures", MeasureViewSet)

urlpatterns = router.urls
