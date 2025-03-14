from django.db import models

# class Comment(models.Model):
#     body = models.TextField(blank=True)
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey("content_type", "object_id")

#     created = models.DateTimeField(auto_now_add=True, null=True)
#     modified = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.body

#     class Meta:
#         ordering = ["-id"]


class Catalog(models.Model):
    name = models.CharField(max_length=140)
    key = models.CharField(max_length=140)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]


class Muscle(models.Model):
    name = models.CharField(max_length=140)
    photo = models.CharField(max_length=140, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
