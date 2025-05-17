from django.db import models

from django.contrib.auth.models import AbstractUser
from core.constants import CLIENT, GENDER_CHOICES, MALE, USER_TYPES_CHOICES


class User(AbstractUser):
    photo = models.ImageField(
        upload_to="users/", default="default.jpg", blank=True, null=True
    )

    gender = models.CharField(max_length=144, choices=GENDER_CHOICES, default=MALE)
    phone = models.IntegerField(default=0)
    age = models.IntegerField(default=0)

    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)

    experience_level = models.CharField(max_length=140, null=True)

    user_type = models.CharField(
        max_length=144, choices=USER_TYPES_CHOICES, default=CLIENT
    )

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.username


class Fcmtoken(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    token = models.CharField(max_length=200, null=True, blank=True)
    device = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
