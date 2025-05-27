from rest_framework.routers import DefaultRouter
from .viewsets import (
    NotificationViewSet,
)

router = DefaultRouter()
router.register("notifications", NotificationViewSet)

urlpatterns = router.urls
