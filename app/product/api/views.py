from rest_framework import (viewsets,
                            generics,
                            permissions,
                            authentication)
from django.shortcuts import get_object_or_404
from django.http import Http404

from .serializers import (
    ProductManageSerializer
)
from product.models.product import Product


class ProductRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductManageSerializer
    queryset = Product.objects.all()

    def get_object(self):
        product_slug = sub_code = self.kwargs.get('slug', None)
        user = self.request.user

        product = Product.objects.get_object_or_none(
            shop=user.staff_profile.shop,
            slug=product_slug
        )

        if product:
            return product
        else:
            raise Http404
