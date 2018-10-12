from django.urls import reverse
from rest_framework.test import APITestCase
from products.models import Product


class ProductsCreateAPITest(APITestCase):
    def setUp(self):
        super().setUp()
        self.view = reverse('api:create')

    def test_create_product(self):
        """
        Test bulk create
        """
        product = {
            'name': 'some name',
            'description': 'some text'
        }
        data = [product] * 3

        response = self.client.post(self.view, data, format='json')
        self.assertEqual(201, response.status_code, response.data)
        product_count = Product.objects.count()
        self.assertEqual(3, product_count, response.data)
