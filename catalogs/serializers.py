from .models import Catalog
from rest_framework import serializers


class CatalogSerializer(serializers.ModelSerializer):
    key_display = serializers.CharField(source='get_key_display', read_only=True)
    created_format = serializers.DateTimeField(source='created', format='%d %m, %Y', read_only=True)

    class Meta:
        model = Catalog
        fields = "__all__"
