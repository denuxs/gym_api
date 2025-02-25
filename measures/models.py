from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Measure(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        # related_name="equipment_catalog_set",
    )
    comment = models.TextField(null=True, blank=True)

    weight = models.FloatField(default=0)

    chest = models.FloatField(default=0)
    abdomen = models.FloatField(default=0)
    back = models.FloatField(default=0)

    arm_left = models.FloatField(default=0)
    arm_right = models.FloatField(default=0)

    leg_left = models.FloatField(default=0)
    leg_right = models.FloatField(default=0)

    waist = models.FloatField(default=0)
    hips = models.FloatField(default=0)

    photo_back = models.CharField(max_length=140, null=True)
    photo_front = models.CharField(max_length=140, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # deleted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ["-id"]
