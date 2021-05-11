from django.db import models
from django.contrib.auth import get_user_model


class ShopStaff(models.Model):
    """ User model for the project """
    ROLE_CHOICE = (
        (1, 'Basic User'),
        (2, 'Owner'),
        (3, 'Manager'),
        (4, 'POS'),
    )

    user_account = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='user_shop'
    )
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICE,
        default=1
    )

    def __str__(self):
        return self.user_account.email
