from django.contrib import admin

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

User = get_user_model()

admin.site.register(User)
admin.site.register(ContentType)
admin.site.register(Permission)

admin.site.unregister(OutstandingToken)
admin.site.register(OutstandingToken)
