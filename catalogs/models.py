from django.db import models


class Catalog(models.Model):
    name = models.CharField(max_length=140)
    key = models.CharField(max_length=140)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # class Meta:
    #     ordering = ["-id"]
