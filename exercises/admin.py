from .models import Exercise
from django.contrib import admin

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("name", )
    list_select_related = ("equipment",)
    list_filter = ("equipment",)

admin.site.register(Exercise, ExerciseAdmin)