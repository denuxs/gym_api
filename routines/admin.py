from comments.models import Comment
from .models import Routine
from django.contrib import admin

# class CommentAdminInline(admin.TabularInline):
#     extra = 1
#     model = Comment
#     # ct_fk_field = "object_id"
#     # ct_field = "content_type"

# class RoutineAdminInline(admin.TabularInline):
#     extra = 1
#     model = RoutineDetail

class RoutineAdmin(admin.ModelAdmin):
    # list_display = ("name", "user",)
    # search_fields = ("name", "user__username")
    list_per_page = 10
    filter_horizontal = ('exercises',)
    # list_select_related = ("user",)
    # list_filter = ("gender",)
    # inlines = (RoutineAdminInline,)

admin.site.register(Routine, RoutineAdmin)