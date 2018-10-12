from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from django import http

from products.models import Product
from api.serializers import ProductSerializer


class ListMixin:
    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            if isinstance(data, list):
                kwargs["many"] = True

        return super().get_serializer(*args, **kwargs)


class ProductObjectMixin:
    def get_object(self):
        ids_list = self.get_update_ids(self.request.data)
        products = Product.objects.filter(id__in=ids_list)
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


class ProductsCreateAPIView(ListMixin, CreateAPIView):
    serializer_class = ProductSerializer


class ProductUpdateAPIView(ListMixin, ProductObjectMixin, UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteAPIView(ListMixin, ProductObjectMixin, DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
