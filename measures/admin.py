
from django.contrib import admin
from .models import Measure

class MeasureAdmin(admin.ModelAdmin):
    list_display = ("user", "created",)

admin.site.register(Measure, MeasureAdmin)