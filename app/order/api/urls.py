from django.urls import path
from .views import (
    OrderCreateView
)

app_name = 'order_api'


urlpatterns = [
    path('create/<slug:shop_slug>/', OrderCreateView.as_view(), name="create"),
]
