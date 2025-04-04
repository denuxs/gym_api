from django.contrib import admin

from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "content",
    )
    # ordering = ["key"]
    # search_fields = ("name",)


admin.site.register(Post, PostAdmin)
