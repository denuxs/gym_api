from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="comments",
    )
    image = models.ImageField(upload_to="comments/", blank=True, null=True)

    content = models.TextField()

    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    parent = models.ForeignKey(
        "self", related_name="children", on_delete=models.PROTECT, blank=True, null=True
    )

    created = models.DateTimeField(auto_now_add=True, null=True)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content


class CommentReplies(models.Model):
    comment = models.ForeignKey(
        Comment,
        on_delete=models.PROTECT,
        related_name="replies",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )
    content = models.TextField()

    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.content
