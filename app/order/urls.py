from django.urls import path

from .views import (
    OrderCreateView,
    OrderListView
)


app_name = 'order'

urlpatterns = [
    path('create/<slug:shop_slug>/', OrderCreateView.as_view(), name='create'),
    path('list/<slug:shop_slug>/', OrderListView.as_view(), name='list'),
]
