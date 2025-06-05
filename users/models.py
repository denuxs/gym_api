from django.db import models
from django.contrib.auth.models import AbstractUser

from companies.models import Company


class User(AbstractUser):
    avatar = models.ImageField(upload_to="users/", blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
