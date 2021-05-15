from django.shortcuts import render
from django.views.generic import (
    TemplateView
)


class TransactionHomeView(TemplateView):
    template_name = 'transaction/home.html'
