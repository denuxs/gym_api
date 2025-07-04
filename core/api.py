from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from catalogs.viewsets import (
    CatalogViewSet,
)

from comments.viewsets import CommentViewSet
from companies.viewsets import (
    CompanyViewSet,
)
from core.auth import CustomTokenObtainPairView
from core.dashboard import DashboardApiView
from exercises.viewsets import ExerciseViewSet
from images.viewsets import ImageViewSet
from measures.viewsets import MeasureViewSet
from notifications.viewsets import NotificationViewSet
from routines.viewsets import RoutineExerciseViewSet, RoutineViewSet, UserRoutineViewSet
from users.viewsets import UserViewSet

# from chatbot.view import ChatbotView

router = DefaultRouter()
router.register("catalogs", CatalogViewSet)
router.register("companies", CompanyViewSet)
router.register("users", UserViewSet)
router.register("user-routines", UserRoutineViewSet)
router.register("comments", CommentViewSet)
router.register("images", ImageViewSet)
router.register("exercises", ExerciseViewSet)
router.register("routines", RoutineViewSet)
router.register("routineexercises", RoutineExerciseViewSet)
router.register("measures", MeasureViewSet)
router.register("notifications", NotificationViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path(
        "login/", CustomTokenObtainPairView.as_view(), name="custom_token_obtain_pair"
    ),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("dashboard/", DashboardApiView.as_view(), name="dashboard"),
    path("token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
    # path("chatbot/", ChatbotView.as_view(), name="chatbot"),
]
