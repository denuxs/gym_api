from comments.models import Comment
from .models import Routine, RoutineDetail
from django.contrib import admin

class CommentAdminInline(admin.TabularInline):
    extra = 1
    model = Comment
    # ct_fk_field = "object_id"
    # ct_field = "content_type"

class RoutineAdminInline(admin.TabularInline):
    extra = 1
    model = RoutineDetail

class RoutineAdmin(admin.ModelAdmin):
    list_display = ("name", )
    # search_fields = ("name", "user__username")
    list_per_page = 10
    # list_select_related = ("user",)
    # list_filter = ("user__username",)
    inlines = (RoutineAdminInline,)

admin.site.register(Routine, RoutineAdmin)