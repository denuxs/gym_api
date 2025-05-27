from rest_framework.routers import DefaultRouter
from .viewsets import (
    ClientViewSet,
)

router = DefaultRouter()
router.register("clients", ClientViewSet)

urlpatterns = router.urls
