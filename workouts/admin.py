from django.contrib import admin
from .models import Workout


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("user", "day")

    list_filter = ("user",)
    filter_horizontal = ("exercises",)


admin.site.register(Workout, WorkoutAdmin)
