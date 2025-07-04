from django.db import models
from django.contrib.auth.models import AbstractUser

from companies.models import Company

ROLE_CHOICES = (
    ("admin", "Admin"),
    ("coach", "Entrenador"),
    ("client", "Cliente"),
)


class User(AbstractUser):
    avatar = models.ImageField(upload_to="users/", blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    coach = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)

    role = models.CharField(max_length=140, choices=ROLE_CHOICES, default="client")
    # created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
