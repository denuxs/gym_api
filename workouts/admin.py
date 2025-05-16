from django.contrib import admin
from .models import Workout


# class WorkoutAdminInline(admin.TabularInline):
#     extra = 1
#     model = WorkoutExcercise


# class WorkoutAdmin(admin.ModelAdmin):
#     list_display = ("title", "user", )

#     list_filter = ("user",)
# inlines = (WorkoutAdminInline,)


# admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Workout)
