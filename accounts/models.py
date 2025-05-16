from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation

# from notifications.models import Notification
from images.models import Image
from django.contrib.contenttypes.models import ContentType


class User(AbstractUser):
    photo = models.ImageField(
        upload_to="users/", default="default.jpg", blank=True, null=True
    )

    gender = models.CharField(max_length=144)
    phone = models.IntegerField(default=0)
    age = models.IntegerField(default=0)

    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)

    experience_level = models.CharField(max_length=140, null=True)

    # notifications = GenericRelation("Notification")

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.username

    # def delete(self, *args, **kwargs):
    #     content = ContentType.objects.get_for_model(User)

    #     Image.objects.filter(
    #         object_id=self.id,
    #         content_type=content,
    #     ).delete()

    #     super().delete(*args, **kwargs)


class Fcmtoken(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    token = models.CharField(max_length=200, null=True, blank=True)
    device = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
