from rest_framework.routers import DefaultRouter
from .viewsets import (
    ImageViewSet,
)

router = DefaultRouter()
router.register("images", ImageViewSet)

urlpatterns = router.urls
