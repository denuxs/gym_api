from django.db import models
from core.constants import GENDER_CHOICES, MALE

from django.contrib.auth import get_user_model

User = get_user_model()


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    gender = models.CharField(max_length=144, choices=GENDER_CHOICES, default=MALE)
    phone = models.IntegerField(default=0)
    age = models.IntegerField(default=0)

    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)

    experience_level = models.CharField(max_length=140, null=True)
    coach = models.ForeignKey(User, on_delete=models.PROTECT, related_name="coach")

    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
