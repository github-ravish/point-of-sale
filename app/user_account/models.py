from django.db import models
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin)
from django.utils import timezone

from user_account.managers import UserAccountManager


class UserAccount(AbstractBaseUser, PermissionsMixin):
    """ User model for the project """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=15, null=True)

    is_phone_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    objects = UserAccountManager()
    