from rest_framework import serializers


from product.models.product import Product
from order.models.order import Order
from order.models.order_item import OrderItem
from shop.models.shop import Shop


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(
        slug_field='slug', queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = ('product', 'quantity',)


class OrderSerializer(serializers.ModelSerializer):
    """This is serializer for subject model"""
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('items', 'order_id', 'price')
        extra_kwargs = {
            'order_id': {'read_only': True},
            'price': {'read_only': True},
        }

    def create(self, validated_data):
        order_item_objects = []
        order_price = 0
        shop = self.context.get('shop')
        for i in validated_data['items']:
            order_price += i['product'].selling_price * i['quantity']
            order_item_objects.append(
                OrderItem.objects.create(
                    product=i['product'], quantity=i['quantity'])
            )

        order_obj = Order.objects.create(
            shop=shop,
            price=order_price
        )
        order_obj.items.set(order_item_objects)
        return order_obj
