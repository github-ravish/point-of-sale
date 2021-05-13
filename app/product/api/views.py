from rest_framework import (viewsets,
                            generics,
                            permissions,
                            authentication)
from django.shortcuts import get_object_or_404
from django.http import Http404, request
from django.conf import settings

from .serializers import (
    ProductManageSerializer
)
from product.models.product import Product
from .permissions import ProductManagePermission


class ProductRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (ProductManagePermission,)
    serializer_class = ProductManageSerializer
    queryset = Product.objects.all()
    roles_allowed = [
        settings.SHOP_ROLE_CHOICE_REVERSE.get('Owner'),
        settings.SHOP_ROLE_CHOICE_REVERSE.get('Manager'),
        settings.SHOP_ROLE_CHOICE_REVERSE.get('POS'),
    ]

    def get_object(self):
        product_slug = self.kwargs.get('product_slug', None)
        shop_slug = self.kwargs.get('shop_slug', None)

        product = Product.objects.get_object_or_none(
            shop__slug=shop_slug,
            slug=product_slug,
        )

        if product:
            return product
        else:
            raise Http404
