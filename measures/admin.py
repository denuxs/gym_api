from django.contrib import admin
from .models import Measure


class MeasureAdmin(admin.ModelAdmin):
    list_display = (
        "client",
        "created",
    )
    # filter_horizontal = ("images",)


admin.site.register(Measure, MeasureAdmin)
