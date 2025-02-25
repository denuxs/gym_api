from .models import Routine
from django.contrib import admin


class RoutineAdmin(admin.ModelAdmin):
    list_per_page = 10
    filter_horizontal = ("exercises",)


admin.site.register(Routine, RoutineAdmin)
