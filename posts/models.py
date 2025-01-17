from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comment

class Post(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # deleted = models.DateTimeField(auto_now=True)
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-id"]
        # permissions = (("can_mark_returned", "Set book as returned"),)