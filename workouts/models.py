from django.db import models
from core.constants import GENDER_CHOICES, MALE, DAYS_OF_WEEK

from exercises.models import Exercise

from django.contrib.auth import get_user_model

User = get_user_model()


class Workout(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    day = models.IntegerField(default=0, choices=DAYS_OF_WEEK)
    photo = models.ImageField(
        upload_to="workouts/", default="default.jpg", blank=True, null=True
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    exercises = models.ManyToManyField(
        Exercise,
        through="WorkoutExcercise",
        related_name="+",
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class WorkoutExcercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    sets = models.IntegerField(default=4)
    repts = models.IntegerField(default=12)
    weight = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.workout.name
