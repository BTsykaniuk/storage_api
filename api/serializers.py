from datetime import datetime

from rest_framework import serializers
from products.models import Product


class ProductListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        out = []
        for item in validated_data:
            product = Product.objects.create(**item)
            product.save()
            out.append(product)
        return out

    def update(self, instance, validated_data):
        product_map = {product.id: product for product in instance}
        data_map = {item['id']: item for item in validated_data}

        out = []
        for product_id, data in data_map.items():
            data['date_updated'] = datetime.today().date()
            product = product_map.get(product_id)
            out.append(self.child.update(product, data))
        return out

    def delete(self, instance):
        for item in instance:
            item.delete()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Product
        fields = '__all__'
        list_serializer_class = ProductListSerializer
