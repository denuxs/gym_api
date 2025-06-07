from rest_framework.routers import DefaultRouter
from .viewsets import (
    CatalogViewSet,
)

router = DefaultRouter()
router.register("catalogs", CatalogViewSet)

# urlpatterns = router.urls
