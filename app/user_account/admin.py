from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Permission

from user_account.models import UserAccount


class CustomUserAccountAdmin(ImportExportModelAdmin, UserAdmin):

    ordering = ['id']
    list_display = ['email']
    list_filter = ('is_active',)
    search_fields = ('email',)
    readonly_fields = ['date_joined', 'last_login', ]
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (_('Personal Info'), {
            'fields': ('first_name', 'last_name', 'phone',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',)
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'phone', 'password1', 'password2')
        }),
    )


admin.site.register(UserAccount, CustomUserAccountAdmin)
admin.site.register(Permission)
