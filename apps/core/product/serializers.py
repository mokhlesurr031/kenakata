from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    # created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image', 'description', 'is_offer_running', 'offer_type', 'offer_rate', 'price_including_offer', 'category_name']

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if instance.is_offer_running:
            if instance.offer_type == 'flat':
                data['price_including_offer'] = instance.price - instance.offer_rate
            elif instance.offer_type == 'percentage':
                discount = (instance.price * instance.offer_rate) / 100
                data['price_including_offer'] = instance.price - discount

        return data