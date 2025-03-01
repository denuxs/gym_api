from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from catalogs.models import Muscle
from comments.models import Comment
from equipments.models import Equipment


class Exercise(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)

    photo = models.CharField(max_length=140, null=True, blank=True)
    video = models.CharField(max_length=140, null=True, blank=True)

    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    muscle = models.ForeignKey(
        Muscle,
        on_delete=models.CASCADE,
    )

    sets = models.IntegerField(default=0)
    repts = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # deleted = models.DateTimeField(auto_now=True)

    comments = GenericRelation(Comment)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["muscle"]
