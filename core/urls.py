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
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

from rest_framework import routers
from comments.viewsets import CommentViewSet
from equipments.viewsets import EquipmentViewSet
from exercises.viewsets import ExerciseViewSet
from accounts.viewsets import UserViewSet, RegisterApiView
from routines.viewsets import RoutineViewSet
from workouts.viewsets import WorkoutViewSet
from measures.viewsets import MeasureViewSet
from catalogs.viewsets import MuscleViewSet
from core.dashboard import DashboardApiView

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"comments", CommentViewSet)
router.register(r"equipments", EquipmentViewSet)
router.register(r"exercises", ExerciseViewSet)
router.register(r"routines", RoutineViewSet)
router.register(r"workouts", WorkoutViewSet)
router.register(r"measures", MeasureViewSet)
router.register(r"muscles", MuscleViewSet)

from django.utils.translation import get_language, gettext as _
from django.conf.urls.i18n import i18n_patterns


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
    path("api/auth/register/", RegisterApiView.as_view(), name="auth_register"),
    path("api/dashboard/", DashboardApiView.as_view(), name="dashboard"),
    # path('i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
