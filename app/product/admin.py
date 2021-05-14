from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from product.models.product import Product


class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
