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
        Test bulk update
        """
        seller = mommy.make('sellers.Seller',
                            name='TestSeller')
        mommy.make('items.Item',
                   name='Some name',
                   seller=seller,
                   _quantity=3)

        product1 = {
            'id': 1,
            'name': 'Updated'
        }
        product2 = {
            'id': 2,
            'name': 'Updated'
        }

        data = [product1, product2]

        response = self.client.patch(self.view, data, format='json')
        self.assertEqual(200, response.status_code, response.data)
        product = Item.objects.all()
        self.assertEqual('Updated', product[0].name, response.data)
        self.assertEqual('Updated', product[1].name, response.data)
        self.assertNotEqual('Updated', product[2].name, response.data)

    def test_update_single_from_multiple(self):
        mommy.make('items.Item',
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
        mommy.make('items.Item',
                   _quantity=2)
        product = {
            'id': 3,
            'name': 'Updated'
        }
        data = [product]
        response = self.client.patch(self.view, data, format='json')
        self.assertEqual(404, response.status_code, response.data)
