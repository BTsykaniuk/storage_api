from datetime import datetime

from rest_framework import serializers
from items.models import Item
from sellers.models import Seller

from utils.serilizer_mixin import DynamicFieldsModelSerializer


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class ItemSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Item
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        if validated_data['description']:
            instance.description = validated_data['description']
        instance.date_updated = datetime.today().date()

        instance.save()

        return instance


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
