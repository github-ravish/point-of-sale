from django.urls import path
from .views import (
    ProductRetrieveUpdateView
)

app_name = 'product_api'


urlpatterns = [
    path('manage/<slug:shop_slug>/<slug:product_slug>/',
         ProductRetrieveUpdateView.as_view(), name="manage"),
]
