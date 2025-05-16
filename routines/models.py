from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comment
from exercises.models import Exercise
from core.constants import WORKOUT_LEVEL, BEGINNER, DAYS_OF_WEEK


class Routine(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(
        upload_to="routines/", default="default.jpg", blank=True, null=True
    )

    level = models.CharField(max_length=140, choices=WORKOUT_LEVEL, default=BEGINNER)

    exercises = models.ManyToManyField(
        Exercise,
        through="RoutineExcercise",
        # related_name="+",
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]


class RoutineExcercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.PROTECT)
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    data = models.JSONField(null=True, blank=True)
    # sets = models.IntegerField(null=True, default=4)
    # repts = models.IntegerField(null=True, default=12)
    # weight = models.IntegerField(null=True, default=0)
    description = models.TextField(null=True, blank=True)
    order = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.routine.title

    class Meta:
        ordering = ["order"]
