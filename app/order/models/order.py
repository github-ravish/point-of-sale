from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from utils.utils import generate_payment_slug

from order.models.order_item import OrderItem
from shop.models.shop import Shop
from shop.managers import CustomManager


class Order(models.Model):

    order_id = models.SlugField()
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name='shop_orders'
    )
    items = models.ManyToManyField(
        OrderItem,
        blank=True,
        related_name='related_order'
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10
    )
    created_at = models.DateTimeField(
        auto_now=True,
    )

    objects = models.Manager()
    shop_owner_objects = CustomManager()

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.order_id = slugify(generate_payment_slug())
        super(Order, self).save(*args, **kwargs)
