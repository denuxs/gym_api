"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)

from django.utils.translation import get_language, gettext as _
from django.conf.urls.i18n import i18n_patterns

from rest_framework import routers, permissions
from comments.viewsets import CommentViewSet

from exercises.viewsets import ExerciseViewSet
from accounts.viewsets import UserViewSet, RegisterApiView, FcmTokenViewSet
from images.viewsets import ImageViewSet
from notifications.viewsets import NotificationViewSet
from posts.viewsets import PostViewSet
from workouts.viewsets import WorkoutViewSet, WorkoutDetailViewSet
from measures.viewsets import MeasureViewSet
from catalogs.viewsets import CatalogViewSet
from core.dashboard import DashboardApiView

router = routers.DefaultRouter()
router.register(r"catalogs", CatalogViewSet)
router.register(r"users", UserViewSet)
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)
router.register(r"images", ImageViewSet)
router.register(r"exercises", ExerciseViewSet)
router.register(r"workouts", WorkoutViewSet)
router.register(r"workouts-detail", WorkoutDetailViewSet)
router.register(r"measures", MeasureViewSet)
router.register(r"notifications", NotificationViewSet)
router.register(r"fcmtokens", FcmTokenViewSet)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="AFIT API",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


def home(request):
    print(get_language())
    message = _("Hello, world")

    return HttpResponse(message)


urlpatterns = [
    path("", include("rest_framework.urls")),
    path("home/", home),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/auth/register/", RegisterApiView.as_view(), name="auth_register"),
    path("api/dashboard/", DashboardApiView.as_view(), name="dashboard"),
    path("api/token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
    # path('i18n/', include('django.conf.urls.i18n')),
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
