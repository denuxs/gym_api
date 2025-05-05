from images.models import Image
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

KEY_CHOICES = (
    ('muscle', "Musculo"),
    ('equipment', "Equipo"),
)
class Catalog(models.Model):
    name = models.CharField(max_length=140)
    key = models.CharField(max_length=140, choices=KEY_CHOICES)
    image = models.ImageField(
        upload_to="catalogs/", blank=True, null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    images = GenericRelation(Image)

    def __str__(self):
        return self.name

    # class Meta:
    #     ordering = ["-id"]
