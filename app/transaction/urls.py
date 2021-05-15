from django.urls import path


from .views import (
    TransactionHomeView
)

app_name = 'tansaction'

urlpatterns = [
    path('create/<slug:order_id>/',
         TransactionHomeView.as_view(), name='home'),
]
