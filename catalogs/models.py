from django.db import models

KEY_CHOICES = (
    ("muscle", "Musculo"),
    ("equipment", "Equipo"),
)


class Catalog(models.Model):
    name = models.CharField(max_length=140)
    key = models.CharField(max_length=140, choices=KEY_CHOICES)
    image = models.ImageField(upload_to="catalogs/", blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
