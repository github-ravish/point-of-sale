from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
)
from django.conf import settings
from django.urls import reverse_lazy

from product.permission import RoleRequiredMixin
from product.models.product import Product
from .forms import ProductModelForm

from shop.models.shop import Shop


class ProductCreateView(RoleRequiredMixin, CreateView):
    form_class = ProductModelForm
    template_name = 'product/create.html'
    success_url = 'static_pages:home'
    roles_required = [
        settings.SHOP_ROLE_CHOICE_REVERSE.get('Owner'),
        settings.SHOP_ROLE_CHOICE_REVERSE.get('Manager'),
    ]

    def form_valid(self, form):
        shop_slug = self.kwargs.get('shop_slug')
        shop = Shop.custom_manager.get_object_or_none(
            shop_staff__user_account=self.request.user,
            slug=shop_slug
        )
        form.instance.shop = shop
        return super(ProductCreateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('product:list', kwargs={'shop_slug': self.kwargs.get('shop_slug')})


class ProductListView(RoleRequiredMixin, ListView):
    template_name = 'product/list.html'
    roles_required = [
        settings.SHOP_ROLE_CHOICE_REVERSE.get('Owner'),
        settings.SHOP_ROLE_CHOICE_REVERSE.get('Manager'),
    ]

    def get_queryset(self):
        shop_slug = self.kwargs.get('shop_slug')
        return Product.objects.filter(
            shop__slug=shop_slug
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop_slug'] = self.kwargs.get('shop_slug')
        return context
