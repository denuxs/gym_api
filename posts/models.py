from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        # related_name="equipment_catalog_set",
    )
    content = models.TextField(null=True, blank=True)
    photo = models.ImageField(
        upload_to="posts/", default="default.jpg", blank=True, null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ["-id"]
