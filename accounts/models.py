from django.db import models

from django.contrib.auth.models import AbstractUser

# from workouts.models import Workout
from core.constants import GENDER_CHOICES, MALE

class User(AbstractUser):
    # email = models.EmailField(
    #     unique=True,
    # )
    photo = models.ImageField(
        upload_to="photos/", default="default.jpg", blank=True, null=True
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, default=MALE)

    # gender = models.ForeignKey(
    #     Catalog,
    #     on_delete=models.CASCADE,
    #     related_name="gender_catalog_set",
    #     null=True,
    #     blank=True,
    # )
    # age = models.IntegerField(default=0)
    # weight = models.IntegerField(default=0)
    # height = models.IntegerField(default=0)

    # workouts = models.ManyToManyField(Workout)

    # username = models.CharField(
    #     max_length=140,
    #     unique=True,
    # )

    # username = None
    # USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = ["username"]

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.username
