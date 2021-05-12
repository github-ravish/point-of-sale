from django.shortcuts import render, redirect
from django.views.generic import (
    TemplateView,
    View
)
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(View):
    template_name = 'static_page/home.html'

    def get(self, request, *args, **kwargs):
        if request.user.user_shop.filter(role=settings.SHOP_ROLE_CHOICE_REVERSE.get('Owner')).exists():
            return redirect('shop:list')
        return render(request, self.template_name)
