from django.db import models
from django.contrib.auth import get_user_model


from product.managers import ProductManager
from shop.models.shop import Shop


class Product(models.Model):

    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name='shop_products',
    )
    slug = models.SlugField()
    name = models.CharField(max_length=64)
    quantity = models.IntegerField()
    cost_price = models.DecimalField(decimal_places=2, max_digits=10)
    selling_price = models.DecimalField(decimal_places=2, max_digits=10)

    objects = ProductManager()

    def __str__(self):
        return self.slug
