from datetime import datetime

from rest_framework import serializers
from items.models import Item
from sellers.models import Seller

from utils.serilizer_mixin import DynamicFieldsModelSerializer


class SellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        fields = '__all__'


class ItemDetailListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        out = []
        for item in validated_data:
            product = Item.objects.create(**item)
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


class ItemSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Item
        fields = '__all__'
        list_serializer_class = ItemDetailListSerializer


class ItemListSerializer(ItemSerializer):
    seller = SellerSerializer()


class SellerListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    items = ItemSerializer(many=True,
                           source='get_items',
                           fields=('id', 'name', 'description', 'date_added', 'date_updated'))

    class Meta:
        model = Seller
        fields = ('id', 'name', 'birthday', 'items')
