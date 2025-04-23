from django.db import models

from django.contrib.auth import get_user_model
import os

User = get_user_model()

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Image(models.Model):
    photo = models.ImageField(
        upload_to="images/", default="default.jpg", blank=True, null=True
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.photo.url

    # class Meta:
    #     ordering = ["-id"]

    def delete(self, *args, **kwargs):
        # Delete the image file if it exists
        if self.photo:
            if os.path.isfile(self.photo.path):
                os.remove(self.photo.path)

        super().delete(*args, **kwargs)
