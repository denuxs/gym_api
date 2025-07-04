from django.db import models
from exercises.models import Exercise
from core.constants import WORKOUT_LEVEL, BEGINNER, DAYS_OF_WEEK

from django.contrib.auth import get_user_model

User = get_user_model()


class Routine(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)

    image = models.ImageField(upload_to="routines/", blank=True, null=True)

    level = models.CharField(max_length=140, choices=WORKOUT_LEVEL, default=BEGINNER)

    exercises = models.ManyToManyField(
        Exercise,
        through="RoutineExcercise",
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class RoutineExcercise(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.PROTECT)
    sets = models.JSONField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.routine.title

    class Meta:
        ordering = ["order"]


class UserRoutine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    routine = models.ForeignKey(Routine, on_delete=models.PROTECT)
    order = models.IntegerField(default=0)
    notes = models.TextField(null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ["order"]
