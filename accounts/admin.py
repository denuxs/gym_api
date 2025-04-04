from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Fcmtoken, User


class UserAdmin(BaseUserAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Fcmtoken)
