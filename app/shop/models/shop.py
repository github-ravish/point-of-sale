import uuid
from django.db import models
from django.contrib.auth import get_user_model

from .shop_staff import ShopStaff
from shop.managers import (
    CustomManager,
)


class Shop(models.Model):

    country = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    area = models.CharField(max_length=64)
    pincode = models.IntegerField()

    name = models.CharField(max_length=128)
    slug = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )

    shop_staff = models.ManyToManyField(
        ShopStaff,
        related_name='user_shop'
    )

    is_active = models.BooleanField(
        default=False
    )

    objects = models.Manager()
    custom_manager = CustomManager()

    def __str__(self):
        return self.name
