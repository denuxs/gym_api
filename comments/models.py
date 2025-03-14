from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    photo = models.ImageField(
        upload_to="comments/", default="default.jpg", blank=True, null=True
    )
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["-id"]
