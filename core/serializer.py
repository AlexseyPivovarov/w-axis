from rest_framework.serializers import ModelSerializer, DateTimeField

from .models import Product, Cart


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'price', 'id')


class CartSerializer(ModelSerializer):

    data = DateTimeField(format="%d %b %Y %H:%M")

    class Meta:
        model = Cart
        fields = ('data', 'product', 'cost', 'id')
