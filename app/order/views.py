from django.shortcuts import render, redirect
from django.views.generic import (
    View,
    ListView
)
from django.conf import settings

from .models.order import Order
from shop.models.shop import Shop
from .permissions import RoleRequiredMixin


class OrderHomeView(RoleRequiredMixin, ListView):
    template_name = "order/home.html"
    roles_required = [
        settings.SHOP_ROLE_CHOICE_REVERSE.get('Owner'),
        settings.SHOP_ROLE_CHOICE_REVERSE.get('Manager'),
        settings.SHOP_ROLE_CHOICE_REVERSE.get('POS'),
    ]

    def get_queryset(self):
        shop = Shop.custom_manager.filter(
            shop_staff__user_account=self.request.user,
            shop_staff__role__in=self.roles_required
        )
        return shop


class OrderCreateView(RoleRequiredMixin, View):
    template_name = 'order/create.html'
    roles_required = [
        settings.SHOP_ROLE_CHOICE_REVERSE.get('Owner'),
        settings.SHOP_ROLE_CHOICE_REVERSE.get('Manager'),
        settings.SHOP_ROLE_CHOICE_REVERSE.get('POS'),
    ]

    def get(self, request, *args, **kwargs):
        context = dict()
        context['shop_slug'] = kwargs.get('shop_slug')
        return render(request, self.template_name, context)


class OrderListView(RoleRequiredMixin, ListView):
    template_name = 'order/list.html'
    roles_required = [
        settings.SHOP_ROLE_CHOICE_REVERSE.get('Owner'),
        settings.SHOP_ROLE_CHOICE_REVERSE.get('Manager'),
        settings.SHOP_ROLE_CHOICE_REVERSE.get('POS'),
    ]

    def get_queryset(self):
        shop_slug = self.kwargs.get('shop_slug')
        return Order.objects.filter(
            shop__slug=shop_slug
        ).order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop_slug'] = self.kwargs.get('shop_slug')
        return context
