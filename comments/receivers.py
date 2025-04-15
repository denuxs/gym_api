from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from accounts.models import Fcmtoken
from exercises.models import Exercise
from notifications.serializers import NotificationSerializer
from .models import Comment
import os
from pathlib import Path
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

import environ

env = environ.Env()

from django.contrib.auth import get_user_model
from django.contrib.humanize.templatetags import humanize

User = get_user_model()

import firebase_admin
from firebase_admin import credentials, messaging

import json

BASE_DIR = Path(__file__).resolve().parent.parent

FIREBASE_ADMIN_CREDENTIAL = os.path.join(BASE_DIR, env("FIREBASE_CREDENTIALS"))

# TODO: valid file path
cred = credentials.Certificate(FIREBASE_ADMIN_CREDENTIAL)
firebase_admin.initialize_app(cred)


@receiver(post_save, sender=Comment)
def create_notification(sender, instance, created, **kwargs):

    if created:
        user = instance.user
        name = user.get_full_name()
        exercise = Exercise.objects.get(id=instance.object_id)
        content = ContentType.objects.get_for_model(Comment)

        notification = Notification.objects.create(
            user=user,
            user_to=exercise.user,
            content_type=content,
            object_id=instance.id,
            # link=f"/exercises/{exercise.id}/comments",
        )
        serializer = NotificationSerializer(notification)

        data = Fcmtoken.objects.filter(user=exercise.user)

        for item in data:
            sendNotification(
                item.token, notification, user, name, exercise, instance, serializer
            )


def sendNotification(
    fcm_token, notification, user, name, exercise, instance, serializer
):
    backend_url = env("BACKEND_URL")
    frontend_url = env("FRONTEND_URL")

    options = messaging.WebpushFCMOptions(
        link=frontend_url + "/workouts",
    )

    # created_format = humanize.naturaltime(instance.created)

    # only string data
    json_data = {
        "id": str(notification.id),
        "username": user.username,
        "photo": backend_url + user.photo.url,
        "comment": instance.content,
        "exercise": exercise.name,
        "created": str(instance.created),
        "is_read": str(False),
    }

    message = messaging.Message(
        notification=messaging.Notification(
            title="AFit Trainer",
            body=f"{name} comento sobre el ejercicio {exercise.name}: {instance.content}",
        ),
        webpush=messaging.WebpushConfig(fcm_options=options),
        data=json_data,
        token=fcm_token,
    )

    messaging.send(message)


@receiver(post_delete, sender=Comment)
def deleteNotification(sender, instance, **kwargs):
    try:
        notification = Notification.objects.get(object_id=instance.id)
        if notification:
            notification.delete()
    except Notification.DoesNotExist:
        return
