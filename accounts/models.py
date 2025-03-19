from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(
        upload_to="users/", default="default.jpg", blank=True, null=True
    )

    phone = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    fcm_token = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.username
