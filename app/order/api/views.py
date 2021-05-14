from rest_framework import (
    generics,
    authentication
)
from django.conf import settings


from .serializers import OrderSerializer
from order.models.order import Order
from shop.models.shop import Shop
from .permissions import OrderPermission


class OrderCreateView(generics.CreateAPIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (OrderPermission,)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    roles_allowed = [
        settings.SHOP_ROLE_CHOICE_REVERSE.get('Owner'),
        settings.SHOP_ROLE_CHOICE_REVERSE.get('Manager'),
        settings.SHOP_ROLE_CHOICE_REVERSE.get('POS'),
    ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update(
            {
                "shop": Shop.custom_manager.get_object_or_none(slug=self.kwargs.get('shop_slug'))
            }
        )
        return context
