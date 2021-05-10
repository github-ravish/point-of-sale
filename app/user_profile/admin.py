from django.contrib import admin

from .models import UserProfile
from user_account.admin import UserAdmin


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    fk_name = 'user_account'
