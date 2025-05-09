from .models import Comment, CommentReplies
from django.contrib import admin


class CommentRepliesAdminInline(admin.TabularInline):
    extra = 1
    model = CommentReplies


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
    inlines = (CommentRepliesAdminInline,)


admin.site.register(Comment, CommentAdmin)
