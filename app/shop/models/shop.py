import uuid
from django.db import models
from django.contrib.auth import get_user_model


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

    is_active = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.name
