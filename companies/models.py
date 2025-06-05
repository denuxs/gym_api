from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone = models.IntegerField(default=0)

    logo = models.ImageField(upload_to="companies/", blank=True, null=True)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
