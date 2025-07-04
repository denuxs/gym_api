from django.contrib import admin

from catalogs.models import Catalog


class CatalogAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "key",
    )
    # ordering = ["key"]
    search_fields = ("name",)
    # list_per_page = 10


admin.site.register(Catalog, CatalogAdmin)
