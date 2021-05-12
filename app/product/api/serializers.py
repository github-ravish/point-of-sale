from rest_framework import serializers


from product.models.product import Product


class ProductManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("slug", "name", "quantity", "cost_price", "selling_price")
