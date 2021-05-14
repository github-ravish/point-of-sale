from django.shortcuts import render, redirect
from django.views.generic import (
    TemplateView,
    View
)
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, View):
    template_name = 'static_page/home.html'
    role_set1 = [
        settings.SHOP_ROLE_CHOICE_REVERSE.get('Owner'),
        settings.SHOP_ROLE_CHOICE_REVERSE.get('Manager'),
    ]

    def get(self, request, *args, **kwargs):
        if request.user.user_shop.filter(role__in=self.role_set1).exists():
            return redirect('shop:list')
        elif request.user.user_shop.filter(role=settings.SHOP_ROLE_CHOICE_REVERSE.get('POS')).exists():
            return redirect('order:home')
        return render(request, self.template_name)
