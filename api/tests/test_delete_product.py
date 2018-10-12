from django.urls import reverse
from rest_framework.test import APITestCase
from model_mommy import mommy
from products.models import Product


class ProductsDeleteAPITest(APITestCase):
    def setUp(self):
        super().setUp()
        self.view = reverse('api:delete')

    def test_delete_product(self):
        """
        Test bulk create
        """
        mommy.make('products.Product',
                   _quantity=5)

        data = [
            {'id': 1},
            {'id': 2},
            {'id': 3}
        ]

        response = self.client.delete(self.view, data, format='json')
        self.assertEqual(204, response.status_code, response.data)
        product_count = Product.objects.count()
        self.assertEqual(2, product_count, response.data)

    def test_delete_not_exist(self):
        mommy.make('products.Product',
                   _quantity=5)

        data = [{'id': 6}]

        response = self.client.delete(self.view, data, format='json')
        self.assertEqual(404, response.status_code, response.data)
        product_count = Product.objects.count()
        self.assertEqual(5, product_count, response.data)
