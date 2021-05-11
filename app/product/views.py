from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    View,
)

from product.permission import RoleRequiredMixin
from product.models.product import Product


class ProductListView(RoleRequiredMixin, ListView):
    template_name = 'product/list.html'

    def get_queryset(self):
        shop_slug = self.kwargs.get('slug')
        return Product.objects.filter(
            shop__slug=shop_slug
        )
