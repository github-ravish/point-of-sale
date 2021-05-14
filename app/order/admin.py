from django.contrib import admin


from order.models.order import Order
from order.models.order_item import OrderItem


admin.site.register(Order)
admin.site.register(OrderItem)
