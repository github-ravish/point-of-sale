from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


class ShopStaff(models.Model):
    """ User model for the project """

    user_account = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='user_shop'
    )
    role = models.PositiveSmallIntegerField(
        choices=settings.SHOP_ROLE_CHOICE,
        default=1
    )

    def __str__(self):
        return self.user_account.email
