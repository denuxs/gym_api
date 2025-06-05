from django.db import models

from core.constants import KEY_CHOICES
from core.utils import custom_upload_to


class Catalog(models.Model):
    name = models.CharField(max_length=140)
    key = models.CharField(max_length=140, choices=KEY_CHOICES)
    image = models.ImageField(upload_to=custom_upload_to, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
