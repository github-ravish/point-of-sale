from django.urls import path
from django.contrib.auth import views as auth_views


from .views import (
    ProductCreateView,
    ProductListView,
)
from shop.views import (
    ShopListView
)

app_name = 'product'

urlpatterns = [
    path('home/', ShopListView.as_view(template_name='product/home.html'), name='home'),
    path('create/<slug:shop_slug>/', ProductCreateView.as_view(), name='create'),
    path('list/<slug:shop_slug>/', ProductListView.as_view(), name='list'),
]
