from django.contrib import admin
from .models import Workout, WorkoutExcercise


class WorkoutAdminInline(admin.TabularInline):
    extra = 1
    model = WorkoutExcercise


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "day")

    list_filter = ("user",)
    inlines = (WorkoutAdminInline,)


admin.site.register(Workout, WorkoutAdmin)
