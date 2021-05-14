from django.urls import path

from .views import (
    OrderCreateView,
    OrderListView
)
from shop.views import (
    ShopListView
)


app_name = 'order'

urlpatterns = [
    path('home/', ShopListView.as_view(template_name='order/home.html'), name='home'),
    path('create/<slug:shop_slug>/', OrderCreateView.as_view(), name='create'),
    path('list/<slug:shop_slug>/', OrderListView.as_view(), name='list'),
]
