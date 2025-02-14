from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
# from comments.models import Comment
from exercises.models import Exercise
from django.db.models import Q
from core.constants import GENDER_CHOICES, MALE, DAYS_OF_WEEK

from django.contrib.auth import get_user_model
User = get_user_model()


class Routine(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    photo = models.CharField(max_length=140)
    # gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, default=MALE)
    # level = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, default=MALE)
    # photo = models.ImageField(
    #     upload_to="workouts/", default="default.jpg", blank=True, null=True
    # )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # deleted = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        # related_name="equipment_catalog_set",
    )

    # day = models.IntegerField(default=0, choices=DAYS_OF_WEEK)

    # exercises = models.ManyToManyField(Exercise)
    # exercises = models.ManyToManyField(
    #     Exercise, through="RoutineDetail", related_name='+',
    # )
    exercises = models.ManyToManyField(Exercise)

    # comments = GenericRelation(Comment)

    def __str__(self):
        # return f"{self.get_gender_display()} / {self.name}"
        return self.name

    class Meta:
        ordering = ["-id"]


# class RoutineDetail(models.Model):
#     routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
#     exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
#     sets = models.IntegerField(default=4)
#     repts = models.IntegerField(default=10)

#     def __str__(self):
#         return self.routine.name
