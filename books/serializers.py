from rest_framework import serializers
from .models import Books


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Books
        fields = '__all__'

    def create(self, validated_data):
        return Books.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.sale_price = validated_data.get('sale_price', instance.sale_price)
        instance.price_on_book = validated_data.get('price_on_book', instance.price_on_book)
        instance.is_new = validated_data.get('is_new', instance.is_new)
        instance.save()

        return instance