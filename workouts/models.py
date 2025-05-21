from django.db import models
from clients.models import Client
from core.constants import DAYS_OF_WEEK

from django.contrib.auth import get_user_model

from routines.models import Routine

User = get_user_model()


class Workout(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    # day = models.IntegerField(default=0, choices=DAYS_OF_WEEK)
    photo = models.ImageField(upload_to="workouts/", blank=True, null=True)

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )

    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
    )

    routines = models.ManyToManyField(Routine)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


def default_sets():
    data = []
    return data.append(dict(repts=0, weight=0))


# class WorkoutExcercise(models.Model):
#     exercise = models.ForeignKey(Exercise, on_delete=models.PROTECT)
#     workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
#     data = models.JSONField(null=True, blank=True)
#     sets = models.IntegerField(null=True, default=4)
#     repts = models.IntegerField(null=True, default=12)
#     weight = models.IntegerField(null=True, default=0)
#     description = models.TextField(null=True, blank=True)
#     order = models.IntegerField(null=True, default=0)

#     def __str__(self):
#         return self.workout.name

#     class Meta:
#         ordering = ["order"]
