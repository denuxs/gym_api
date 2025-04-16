from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Fcmtoken, User
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from rest_framework_simplejwt.token_blacklist.admin import OutstandingTokenAdmin


class UserAdmin(BaseUserAdmin):
    pass


class JwtToken(OutstandingToken):
    class Meta:
        proxy = True


class CustomOutstandingTokenAdmin(OutstandingTokenAdmin):

    def has_delete_permission(self, *args, **kwargs):
        return True


admin.site.register(User, UserAdmin)
admin.site.register(Fcmtoken)
admin.site.register(ContentType)
admin.site.register(Permission)
# admin.site.register(JwtToken)

admin.site.unregister(OutstandingToken)
admin.site.register(OutstandingToken)
