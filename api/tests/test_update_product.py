from django.urls import reverse
from rest_framework.test import APITestCase
from model_mommy import mommy
from products.models import Product


class ProductsUpdateAPITest(APITestCase):
    def setUp(self):
        super().setUp()
        self.view = reverse('api:update')

    def test_update_product(self):
        """
        Test bulk create
        """
        mommy.make('products.Product',
                   name='Some name')

        product = {
            'id': 1,
            'name': 'Updated'
        }
        data = [product]

        response = self.client.patch(self.view, data, format='json')
        self.assertEqual(200, response.status_code, response.data)
        product = Product.objects.get(id=1)
        self.assertEqual('Updated', product.name, response.data)

    def test_update_single_from_multiple(self):
        mommy.make('products.Product',
                   _quantity=2)
        product = {
            'id': 1,
            'name': 'Updated'
        }
        data = [product]

        response = self.client.patch(self.view, data, format='json')
        self.assertEqual(200, response.status_code, response.data)
        product = Product.objects.all()
        self.assertEqual('Updated', product[0].name, response.data)
        self.assertNotEqual('Updated', product[1].name, response.data)

    def update_not_exist(self):
        mommy.make('products.Product',
                   _quantity=2)
        product = {
            'id': 3,
            'name': 'Updated'
        }
        data = [product]
        response = self.client.patch(self.view, data, format='json')
        self.assertEqual(404, response.status_code, response.data)