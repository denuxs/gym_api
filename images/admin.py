from .models import Image
from django.contrib import admin


class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "content_type", "object_id")


admin.site.register(Image, ImageAdmin)
