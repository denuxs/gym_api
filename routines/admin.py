from .models import Routine, RoutineExcercise, UserRoutine
from django.contrib import admin


class RoutineAdminInline(admin.TabularInline):
    extra = 1
    model = RoutineExcercise


class RoutineAdmin(admin.ModelAdmin):
    # list_display = ("name", "user", "day")

    # list_filter = ("user",)
    inlines = (RoutineAdminInline,)


admin.site.register(Routine, RoutineAdmin)
admin.site.register(UserRoutine)
