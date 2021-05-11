from django.urls import path


from .views import (
    ShopCreateView,
    ShopListView,
    ShopDetailView
)

app_name = 'shop'

urlpatterns = [
    path('create/', ShopCreateView.as_view(), name='create'),
    path('list/', ShopListView.as_view(), name='list'),
    path('detail/<slug:slug>/', ShopDetailView.as_view(), name='detail'),
]
