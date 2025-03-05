from django.db import models

from django.contrib.auth import get_user_model
import os
from uuid import uuid4

User = get_user_model()


def custom_upload(path):
    def wrapper(instance, filename):
        ext = filename.split(".")[-1]
        if instance.pk:
            filename = "{}.{}".format(instance.pk, ext)
        else:
            filename = "{}.{}".format(uuid4().hex, ext)
        return os.path.join(path, filename)

    return wrapper


class Measure(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        # related_name="equipment_catalog_set",
    )
    comment = models.TextField(null=True, blank=True)

    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)

    chest = models.FloatField(default=0)
    abdomen = models.FloatField(default=0)
    back = models.FloatField(default=0)

    arm_left = models.FloatField(default=0)
    arm_right = models.FloatField(default=0)

    forearm = models.FloatField(default=0)

    leg_left = models.FloatField(default=0)
    leg_right = models.FloatField(default=0)

    waist = models.FloatField(default=0)
    hips = models.FloatField(default=0)

    glutes = models.FloatField(default=0)

    photo_back = models.ImageField(
        upload_to=custom_upload("measures/back"),
        default="default.jpg",
        blank=True,
        null=True,
    )

    photo_front = models.ImageField(
        upload_to=custom_upload("measures/front"),
        default="default.jpg",
        blank=True,
        null=True,
    )

    photo_left = models.ImageField(
        upload_to=custom_upload("measures/left"),
        default="default.jpg",
        blank=True,
        null=True,
    )

    photo_right = models.ImageField(
        upload_to=custom_upload("measures/right"),
        default="default.jpg",
        blank=True,
        null=True,
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # deleted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ["-id"]
