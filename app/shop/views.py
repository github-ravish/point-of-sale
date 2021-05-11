from django.shortcuts import render
from django.views.generic import (
    CreateView,
)
from django.urls import reverse_lazy


from .models.shop import Shop
from .forms import ShopModelForm


class ShopCreateView(CreateView):
    template_name = 'shop/create.html'
    model = Shop
    form_class = ShopModelForm
    success_url = reverse_lazy("static_page:home")

    def get_form_kwargs(self):
        kwargs = super(ShopCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
