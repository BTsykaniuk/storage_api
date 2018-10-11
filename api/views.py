from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from products.models import Product
from api.serializers import ProductSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
