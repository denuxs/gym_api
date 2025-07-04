from catalogs.models import Catalog
from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Exercise(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)

    image = models.ImageField(upload_to="exercises/", blank=True, null=True)
    video_url = models.CharField(max_length=140, null=True)

    equipment = models.ForeignKey(
        Catalog,
        on_delete=models.PROTECT,
        related_name="equipment_catalog_set",
    )
    muscle = models.ForeignKey(
        Catalog,
        on_delete=models.PROTECT,
        related_name="muscle_catalog_set",
    )
    secondary_muscle = models.JSONField(null=True, blank=True, default=list)

    user = models.ForeignKey(User, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # deleted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
