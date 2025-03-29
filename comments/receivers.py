from django.dispatch import receiver
from django.db.models.signals import post_save

from exercises.models import Exercise
from .models import Comment
import os
from pathlib import Path

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
        user = instance.user.get_full_name()
        exercise = Exercise.objects.get(id=instance.object_id)

        # TO DO
        owner = User.objects.get(id=exercise.user_id)

        message = messaging.Message(
            notification=messaging.Notification(
                title="AFit Trainer",
                body=f"{user} comento sobre el ejercicio {exercise.name}: {instance.content}",
            ),
            token=owner.fcm_token,
        )

        response = messaging.send(message)
        print(response)
