from django.contrib import admin
from .models import Workout


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "day")
    list_filter = ("user",)
    filter_horizontal = ("routines",)


admin.site.register(Workout, WorkoutAdmin)
