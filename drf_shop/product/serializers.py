from rest_framework import serializers

from .models import Producer, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )

    def create(self, validated_data):
        producer = Product.objects.create(**validated_data)
        return producer

class ProducerSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Producer
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products"
        )

    def create(self, validated_data):
        producer = Producer.objects.create(**validated_data)
        return producer