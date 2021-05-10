from django.shortcuts import render, redirect
from django.views.generic import (
    TemplateView,
    View
)
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(View):
    template_name = 'static_page/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
