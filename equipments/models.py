from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    weight = models.IntegerField(default=0)
    photo = models.ImageField(
        upload_to="equipments/", default="default.jpg", blank=True, null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-id"]