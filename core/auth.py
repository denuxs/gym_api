from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data["access"]
        refresh_token = response.data["refresh"]

        response.set_cookie(
            key="access_token",
            value=token,
            httponly=True,
            secure=settings.DEBUG is False,
            samesite="Strict",
            max_age=15 * 60,  # 15 minutos
        )

        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,
            secure=settings.DEBUG is False,
            samesite="Strict",
            max_age=24 * 60 * 60,  # 1 día
        )

        response.data = {"message": "Login successful"}
        return response
