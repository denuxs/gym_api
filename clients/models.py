from django.db import models
from django.contrib.auth.models import AbstractUser

# from django.contrib.auth.models import User
from core.constants import GENDER_CHOICES, MALE

from django.contrib.auth import get_user_model

User = get_user_model()


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    photo = models.ImageField(
        upload_to="clients/", default="default.jpg", blank=True, null=True
    )

    gender = models.CharField(max_length=144, choices=GENDER_CHOICES, default=MALE)
    phone = models.IntegerField(default=0)
    age = models.IntegerField(default=0)

    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)

    experience_level = models.CharField(max_length=140, null=True)

    # class Meta:
    #     ordering = ["-id"]

    def __str__(self):
        return self.user.username
