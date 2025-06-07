from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from django.utils.translation import get_language
from django.utils.translation import gettext as _
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

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
    path("api/", include("core.api")),
    # path("api-auth", include("rest_framework.urls")),
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
