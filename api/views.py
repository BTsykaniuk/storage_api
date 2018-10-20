from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from items.models import Item
from sellers.models import Seller
from api.serializers import ItemSerializer,  ItemListSerializer, SellerListSerializer


class ItemListAPIView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer


class ItemsCreateAPIView(CreateAPIView):
    serializer_class = ItemSerializer


class ItemsUpdateAPIView(UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemsDeleteAPIView(DestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class SellerListAPIView(ListAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerListSerializer
