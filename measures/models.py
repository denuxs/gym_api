from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()

class Measure(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)

    chest = models.CharField(max_length=140)
    back = models.CharField(max_length=140)
    arm = models.CharField(max_length=140)
    leg = models.CharField(max_length=140)
    waist = models.CharField(max_length=140)

    photo = models.ImageField(
        upload_to="measures/", default="default.jpg", blank=True, null=True
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        # related_name="equipment_catalog_set",
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # deleted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
       