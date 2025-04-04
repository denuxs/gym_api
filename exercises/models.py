from catalogs.models import Catalog
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from comments.models import Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class Exercise(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)

    image = models.ImageField(
        upload_to="exercises/", default="default.jpg", blank=True, null=True
    )

    equipment = models.ForeignKey(
        Catalog,
        on_delete=models.CASCADE,
        related_name="equipment_catalog_set",
    )

    muscle = models.ForeignKey(
        Catalog,
        on_delete=models.CASCADE,
        related_name="muscle_catalog_set",
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # deleted = models.DateTimeField(auto_now=True)

    comments = GenericRelation(Comment)

    def __str__(self):
        return self.name

    # class Meta:
    #     ordering = ["muscle"]
