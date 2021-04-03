from .models import Product
from categories.models import Category
from subcategories.models import Subcategory
from rest_framework import serializers


class CategoryItemSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
    class Meta:
        model = Subcategory
        fields = ['name','category']

    
class ProductSerializer(serializers.ModelSerializer):
    subcategory = CategoryItemSerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = (
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
        )

class ProductSerializerSave(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'