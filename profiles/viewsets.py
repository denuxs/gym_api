from rest_framework import viewsets, filters

from profiles.serializers import ProfileSerializer

from .models import Profile


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
