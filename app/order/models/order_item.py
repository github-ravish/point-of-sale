from django.db import models

from product.models.product import Product


class OrderItem(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="order_items"
    )
    quantity = models.IntegerField()
