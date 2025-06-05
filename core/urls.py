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

from rest_framework import permissions
from core.dashboard import DashboardApiView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="AFIT API",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.IsAdminUser,),
)


def home(request):
    return HttpResponse("ok")


urlpatterns = [
    path("", home, name="home"),
    path("afit/", admin.site.urls),
    path("api/", include("companies.urls")),
    path("api/", include("catalogs.urls")),
    path("api/", include("users.urls")),
    path("api/", include("comments.urls")),
    path("api/", include("images.urls")),
    path("api/", include("exercises.urls")),
    path("api/", include("routines.urls")),
    path("api/", include("measures.urls")),
    path("api/", include("notifications.urls")),
    path("api/", include("clients.urls")),
    path("api/", include("workouts.urls")),
    path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/dashboard/", DashboardApiView.as_view(), name="dashboard"),
    path("api/token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
    path("api-auth", include("rest_framework.urls")),
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
