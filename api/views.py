from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from django import http

from items.models import Item
from api.serializers import ItemSerializer


class ListMixin:
    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            if isinstance(data, list):
                kwargs["many"] = True

        return super().get_serializer(*args, **kwargs)


class ItemsObjectMixin:
    def get_object(self):
        ids_list = self.get_update_ids(self.request.data)
        products = Item.objects.filter(id__in=ids_list)
        if products:
            return products
        else:
            raise http.Http404

    @staticmethod
    def get_update_ids(data):
        ids = []
        for item in data:
            ids.append(item['id'])
        return ids


class ItemsCreateAPIView(ListMixin, CreateAPIView):
    serializer_class = ItemSerializer


class ItemsUpdateAPIView(ListMixin, ItemsObjectMixin, UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemsDeleteAPIView(ListMixin, ItemsObjectMixin, DestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
