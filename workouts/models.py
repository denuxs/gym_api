from django.db import models
from django.contrib.auth import get_user_model

from routines.models import Routine

User = get_user_model()


class Workout(models.Model):
    name = models.CharField(max_length=140, default="GYM")
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(
        upload_to="workouts/", default="default.jpg", blank=True, null=True
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        # related_name="equipment_catalog_set",
    )

    routines = models.ManyToManyField(Routine)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # deleted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
