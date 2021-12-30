from rest_framework import serializers
from .models import *


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeVarient
        fields = '__all__'
class ColorSeralizer(serializers.ModelSerializer):
    class Meta:
        model = ColorVariant
        fields = '__all__'

class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantityVariant
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    category = CategorySerializer()
    quantity_type = QuantitySerializer()
    color_type = ColorSeralizer()
    size_type = SizeSerializer()
    class Meta:
        model = Products
        fields = '__all__'
        # exclude = ['id']
