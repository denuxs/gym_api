from .models import Exercise
from django.contrib import admin
from django.utils.html import mark_safe


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("name", "muscle", "equipment",)
    list_select_related = ("equipment", "muscle",)
    # list_filter = ("muscle",)
    # readonly_fields = ("photo_preview", "video_preview")

    # @mark_safe
    # def photo_preview(self, obj):
    #     return f'<a href="{obj.photo.url}" target="_blank"><img src="{obj.photo.url}" width="200" /></a>'

    # @mark_safe
    # def video_preview(self, obj):
    #     # return f'<iframe src="http://www.youtube.com/embed/W7qWa52k-nE" width="250"></iframe>'
    #     return f'<iframe src="https://drive.google.com/file/d/1AuLEp8WFRu8fuD8ieZfLEZVl3egptWgi/preview" width="600" height="400"></iframe>'


admin.site.register(Exercise, ExerciseAdmin)
