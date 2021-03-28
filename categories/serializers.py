from .models import Category
from subcategories.models import Subcategory
from rest_framework import serializers

class SubcategoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('id', 'name')

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategoryItemSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'subcategories'
        )