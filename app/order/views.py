from django.shortcuts import render
from django.views.generic import (
    View,
)


class OrderCreateView(View):
    template_name = 'order/create.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        context['shop_slug'] = kwargs.get('shop_slug')
        return render(request, self.template_name, context)
