from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Notification(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="notifications",
    )
    content = models.TextField(null=True, blank=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    is_read = models.BooleanField(default=False)
    # link = models.CharField(max_length=255, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username
