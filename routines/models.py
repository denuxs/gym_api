from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comment
from exercises.models import Exercise


class Routine(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    photo = models.CharField(max_length=140, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    exercises = models.ManyToManyField(Exercise)

    comments = GenericRelation(Comment)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
