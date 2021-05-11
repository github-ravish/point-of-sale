from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView
)
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


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
    ]

    def get_queryset(self):
        return Shop.custom_manager.filter(
            shop_staff__user_account=self.request.user,
            shop_staff__role__in=self.roles_required
        )
