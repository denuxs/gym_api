from django.db import models
from clients.models import Client
from routines.models import Routine

from django.contrib.auth import get_user_model

User = get_user_model()


class Workout(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="workouts/", blank=True, null=True)

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
    )

    routines = models.ManyToManyField(Routine)

    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
