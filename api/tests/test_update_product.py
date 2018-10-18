from django.urls import reverse
from rest_framework.test import APITestCase
from model_mommy import mommy
from items.models import Item


class ProductsUpdateAPITest(APITestCase):
    def setUp(self):
        super().setUp()
        self.view = reverse('api:update')

    def test_update_product(self):
        """
        Test bulk create
        """
        mommy.make('items.Product',
                   name='Some name')

        product = {
            'id': 1,
            'name': 'Updated'
        }
        data = [product]

        response = self.client.patch(self.view, data, format='json')
        self.assertEqual(200, response.status_code, response.data)
        product = Item.objects.get(id=1)
        self.assertEqual('Updated', product.name, response.data)

    def test_update_single_from_multiple(self):
        mommy.make('items.Product',
                   _quantity=2)
        product = {
            'id': 1,
            'name': 'Updated'
        }
        data = [product]

        response = self.client.patch(self.view, data, format='json')
        self.assertEqual(200, response.status_code, response.data)
        product = Item.objects.all()
        self.assertEqual('Updated', product[0].name, response.data)
        self.assertIsNotNone(product[0].date_updated, response.data)
        self.assertIsNone(product[1].date_updated, response.data)

    def test_update_not_exist(self):
        mommy.make('items.Product',
                   _quantity=2)
        product = {
            'id': 3,
            'name': 'Updated'
        }
        data = [product]
        response = self.client.patch(self.view, data, format='json')
        self.assertEqual(404, response.status_code, response.data)
