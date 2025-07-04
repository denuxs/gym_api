from django.db import models

from django.contrib.auth import get_user_model
import os
from uuid import uuid4

User = get_user_model()


def measure_directory_path(instance, filename):
    ext = filename.split(".")[-1]
    if instance.pk:
        filename = "{}.{}".format(instance.pk, ext)
    else:
        filename = "{}.{}".format(uuid4().hex, ext)

    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "measures/user_{0}/{1}".format(instance.user.id, filename)


# def custom_upload(path):
#     def wrapper(instance, filename):
#         ext = filename.split(".")[-1]
#         if instance.pk:
#             filename = "{}.{}".format(instance.pk, ext)
#         else:
#             filename = "{}.{}".format(uuid4().hex, ext)
#         return os.path.join(path, filename)

#     return wrapper


def default_muscles():
    return dict(
        weight=0,
        chest=0,
        abdomen=0,
        back=0,
        arm_left=0,
        arm_right=0,
        forearm=0,
        leg_left=0,
        leg_right=0,
        waist=0,
        hips=0,
        glutes=0,
    )


class Measure(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    comment = models.TextField(null=True, blank=True)
    measures = models.JSONField(null=True, blank=True, default=default_muscles)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    deleted = models.DateTimeField(null=True, blank=True)

    # def __str__(self):
    #     return self.client
