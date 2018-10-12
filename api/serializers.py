from rest_framework import serializers
from products.models import Product


class ProductListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        products = [Product(**item) for item in validated_data]
        return Product.objects.bulk_create(products)

    def update(self, instance, validated_data):
        product_map = {product.id: product for product in instance}
        data_map = {item['id']: item for item in validated_data}

        out = []
        for product_id, data in data_map.items():
            product = product_map.get(product_id)
            out.append(self.child.update(product, data))
        return out

    def delete(self, instance):
        for item in instance:
            item.delete()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'date_added', 'date_updated')
        list_serializer_class = ProductListSerializer
