from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=140)
    photo = models.CharField(max_length=140, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
