from django.shortcuts import render
from django.db.models import F
from django.views.generic import (
    CreateView,
    ListView,
    DetailView
)
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum


from .models.shop import Shop
from .forms import ShopModelForm
from .permissions import RoleRequiredMixin


class ShopCreateView(LoginRequiredMixin, CreateView):
    template_name = 'shop/create.html'
    model = Shop
    form_class = ShopModelForm
    success_url = reverse_lazy("shop:list")

    def get_form_kwargs(self):
        kwargs = super(ShopCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class ShopListView(RoleRequiredMixin, ListView):
    template_name = "shop/list.html"
    roles_required = [
        settings.SHOP_ROLE_CHOICE_REVERSE.get('Owner'),
        settings.SHOP_ROLE_CHOICE_REVERSE.get('Manager'),
    ]

    def get_queryset(self):
        return Shop.custom_manager.filter(
            shop_staff__user_account=self.request.user,
            shop_staff__role__in=self.roles_required
        )

    def get_context_data(self, **kwargs):
        context = super(ShopListView, self).get_context_data(**kwargs)
        shop_list = context['shop_list']
        context['shop_list'] = shop_list.annotate(
            gross_sales_val=Sum('shop_orders__price'),
            net_margin=Sum(
                (F('shop_orders__items__product__selling_price') -
                 F('shop_orders__items__product__cost_price'))
            ),
            gross_profit=Sum(
                (F('shop_orders__items__product__selling_price') -
                 F('shop_orders__items__product__cost_price')) *
                F('shop_orders__items__quantity')
            )
        )
        return context


class ShopDetailView(RoleRequiredMixin, DetailView):
    template_name = "shop/detail.html"
    roles_required = [
        settings.SHOP_ROLE_CHOICE_REVERSE.get('Owner'),
        settings.SHOP_ROLE_CHOICE_REVERSE.get('Manager'),
    ]

    def get_object(self, *args, **kwargs):
        shop_slug = self.kwargs.get('slug')
        shop = Shop.custom_manager.get_object_or_none(
            slug=shop_slug,
            shop_staff__user_account=self.request.user,
            shop_staff__role__in=self.roles_required,
        )
        return shop
