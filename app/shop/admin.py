from django.contrib import admin

from .models.shop import Shop
from user_profile.admin import UserProfileShopInline


class ShopAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    inlines = [UserProfileShopInline, ]


admin.site.register(Shop, ShopAdmin)
