from .models import Comment
from django.contrib import admin


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "content",
        "user",
        "content_type",
        "object_id",
        "created",
    )
    list_per_page = 10
    list_select_related = ("user",)
    list_filter = ("user__username",)


admin.site.register(Comment, CommentAdmin)
