from django.contrib import admin

from .models.shop import Shop
from shop.models.shop_staff import ShopStaff


class ShopStaffInline(admin.TabularInline):
    model = Shop.shop_staff.through


class ShopAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    inlines = [ShopStaffInline, ]
    list_display = ('name', 'get_address')
    exclude = ('shop_staff',)

    def get_address(self, shop):
        return shop.state + ', ' + shop.area

    get_address.short_description = 'Address'


admin.site.register(Shop, ShopAdmin)
admin.site.register(ShopStaff)
