from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comment
from equipments.models import Equipment

CHEST = "CHEST"
LEG = "LEG"
BACK = "BACK"
ARM = "ARM"

MUSCLE_CHOICES = (
    (CHEST, "Pecho"),
    (BACK, "Espalda"),
    (ARM, "Brazo"),
    # (ABDOMEN, "Abdomen"),
    # (SHOULDER, "Hombro"),   
    # (WAIST, "Cintura"),
    (LEG, "Pierna"),
    
)

class Exercise(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(
        upload_to="exercises/photos", default="default.jpg", blank=True, null=True
    )
    video = models.FileField(
        upload_to="exercises/videos", default="default.jpg", blank=True, null=True
    )
    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        related_name="equipment_catalog_set",
        null=True,
        blank=True,
    )
    muscle = models.CharField(max_length=10, choices=MUSCLE_CHOICES)

    # level = models.ForeignKey(
    #     Catalog,
    #     on_delete=models.CASCADE,
    #     related_name="level_catalog_set",
    #     limit_choices_to=Q(category_id=LEVEL),
    #     null=True,
    #     blank=True,
    # )
    # goal = models.ForeignKey(
    #     Catalog,
    #     on_delete=models.CASCADE,
    #     related_name="goal_catalog_set",
    #     limit_choices_to=Q(category_id=GOAL),
    #     null=True,
    #     blank=True,
    # )

    # sets = models.IntegerField(default=0)
    # repts = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # deleted = models.DateTimeField(auto_now=True)

    comments = GenericRelation(Comment)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
