from .models import Exercise
from django.contrib import admin


class ExerciseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "muscle",
        "equipment",
    )
    list_select_related = (
        "equipment",
        "muscle",
    )


admin.site.register(Exercise, ExerciseAdmin)
