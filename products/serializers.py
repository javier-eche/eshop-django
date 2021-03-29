from .models import Product
from categories.models import Category
from subcategories.models import Subcategory
from rest_framework import serializers

class SubcategoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('pk', 'name')


class CategoryItemSerializer(serializers.ModelSerializer):
    subcategories = SubcategoryItemSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Category
        fields = ('id', 'name', 'subcategories')

    
class ProductSerializer(serializers.ModelSerializer):
    category = CategoryItemSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Product
        fields = (
            'pk',
            'category',
            'image1',
            'image2',
            'image3',
            'image4',
            'image5',
            'price',
            'discount',
            'description',
            'brand'
        )

class ProductSerializerSave(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'