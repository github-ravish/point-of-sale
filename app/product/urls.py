from django.urls import path
from django.contrib.auth import views as auth_views


from .views import (
    ProductListView
)

app_name = 'product'

urlpatterns = [
    path('list/<slug:slug>/', ProductListView.as_view(), name='list'),
]
