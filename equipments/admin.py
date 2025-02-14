from .models import Equipment
from django.contrib import admin

from django.utils.html import mark_safe


# admin.site.register(Equipment)
@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass
    # list_display = ["image_tag", "name", "edit"]
    # list_display_links = ("edit", )
    # readonly_fields = ("thumbnail_preview",)

    # def image_tag(self, obj):
    #     return mark_safe('<img src="%s" width ="50" height="50"/>' % (obj.photo.url))

    # @mark_safe
    # def thumbnail_preview(self, obj):
    #     return f'<a href="{obj.photo.url}" target="_blank"><img src="{obj.photo.url}" width ="100" height="100"/></a>'

    # def edit(self, obj):
    #     return "Edit"