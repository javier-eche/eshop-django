from .models import Subcategory
from rest_framework import serializers
from categories.models import Category


class SubcategorySerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'category'
        )

class SubcategorySerializerSave(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'