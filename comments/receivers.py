from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from accounts.models import Fcmtoken
from exercises.models import Exercise
from .models import Comment
import os
from pathlib import Path
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

import environ

env = environ.Env()

from django.contrib.auth import get_user_model

User = get_user_model()

import firebase_admin
from firebase_admin import credentials, messaging

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

        Notification.objects.create(
            user=user,
            user_to=exercise.user,
            content_type=content,
            object_id=instance.id,
            # link=f"/exercises/{exercise.id}/comments",
        )

        data = Fcmtoken.objects.filter(user=exercise.user)

        for item in data:
            sendNotification(item.token, name, exercise, instance)


def sendNotification(fcm_token, name, exercise, instance):
    frontendUrl = env("FRONTEND_URL")
    options = messaging.WebpushFCMOptions(
        link=frontendUrl + "/workouts",
    )
    message = messaging.Message(
        notification=messaging.Notification(
            title="AFit Trainer",
            body=f"{name} comento sobre el ejercicio {exercise.name}: {instance.content}",
        ),
        webpush=messaging.WebpushConfig(fcm_options=options),
        data={
            "link": frontendUrl + "/workouts",
            "title": "AFit Trainer",
            "body": f"{name} comento sobre el ejercicio {exercise.name}: {instance.content}",
        },
        token=fcm_token,
    )

    messaging.send(message)


@receiver(post_delete, sender=Comment)
def deleteNotification(sender, instance, **kwargs):
    notification = Notification.objects.get(pk=instance.id)
    notification.delete()
