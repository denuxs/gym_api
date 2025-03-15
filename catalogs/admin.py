from django.contrib import admin

from catalogs.models import Catalog


class CatalogAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "key",
    )
    ordering = ["key"]
    search_fields = ("name",)


admin.site.register(Catalog, CatalogAdmin)
