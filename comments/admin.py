from .models import Comment
from django.contrib import admin

class CommentAdmin(admin.ModelAdmin):
    list_display = ("body", "user",)
    # search_fields = ("name", "user__username")
    list_per_page = 10
    list_select_related = ("user",)
    list_filter = ("user__username",)


admin.site.register(Comment, CommentAdmin)
