from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from product.models.product import Product


admin.site.register(ImportExportModelAdmin, Product)
