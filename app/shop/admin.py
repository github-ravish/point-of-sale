from django.contrib import admin

from .models.shop import Shop
from user_profile.admin import UserProfileInline


class ShopAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    inlines = [UserProfileInline, ]


admin.site.register(Shop, ShopAdmin)
