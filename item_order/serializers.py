from .models import Item
from rest_framework import serializers
from products.models import Product
from subcategories.models import Subcategory


class CategoryItemSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
    class Meta:
        model = Subcategory
        fields = ['name','category']


class ProductItemSerializer(serializers.ModelSerializer):
    subcategory = CategoryItemSerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = [
            'pk',
            'subcategory',
            'image1',
            'image2',
            'image3',
            'image4',
            'image5',
            'price',
            'discount',
            'description',
            'brand'
        ]


class ItemSerializer(serializers.ModelSerializer):
    product = ProductItemSerializer(many=False, read_only=True)
    class Meta:
        model = Item
        fields = ['pk', 'product']


class ItemSerializerSave(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'