from django.urls import path

from .views import (
    OrderCreateView,
    OrderListView,
    OrderHomeView
)
from shop.views import (
    ShopListView
)


app_name = 'order'

urlpatterns = [
    path('home/', OrderHomeView.as_view(), name='home'),
    path('create/<slug:shop_slug>/', OrderCreateView.as_view(), name='create'),
    path('list/<slug:shop_slug>/', OrderListView.as_view(), name='list'),
]
