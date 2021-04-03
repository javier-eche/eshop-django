from .models import Order
from rest_framework import serializers
from item_order.models import Item
from products.models import Product

class ProductItemOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price')


class ItemOrderSerializer(serializers.ModelSerializer):
    product = ProductItemOrderSerializer(many=False)
    class Meta:
        model = Item
        fields = ['product']


class OrderSerializer(serializers.ModelSerializer):
    items_order = ItemOrderSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Order
        fields = [
            'pk',
            'user_name',
            'user_email',
            'user_dni',
            'items_order',
            'amount',
            'created_at',
        ]


class OrderSerializerSave(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'