from django.contrib import admin

from .models import UserProfile
from user_account.admin import UserAdmin


class UserProfileShopInline(admin.StackedInline):
    model = UserProfile


class UserProfileUserAccountInline(admin.StackedInline):
    model = UserProfile
    fk_name = 'user_account'
