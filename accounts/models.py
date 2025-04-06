from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation

# from notifications.models import Notification


class User(AbstractUser):
    photo = models.ImageField(
        upload_to="users/", default="default.jpg", blank=True, null=True
    )

    gender = models.CharField(max_length=144)
    phone = models.IntegerField(default=0)
    age = models.IntegerField(default=0)

    # notifications = GenericRelation("Notification")

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.username


class Fcmtoken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=200, null=True, blank=True)
    device = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
