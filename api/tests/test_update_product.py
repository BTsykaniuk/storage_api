from django.urls import reverse
from rest_framework.test import APITestCase
from model_mommy import mommy
from items.models import Item


class ProductsUpdateAPITest(APITestCase):
    def setUp(self):
        super().setUp()

    def test_update_product(self):
        seller = mommy.make('sellers.Seller',
                            name='TestSeller')
        mommy.make('items.Item',
                   name='Some name',
                   seller=seller,
                   _quantity=2)

        data = {'pk': 1}
        view = reverse('api:update', kwargs=data)

        product = {
            'name': 'Updated',
            'description': 'Updated'
        }

        response = self.client.patch(view, product, format='json')
        self.assertEqual(200, response.status_code, response.data)
        product = Item.objects.all()
        self.assertEqual('Updated', product[0].name, response.data)
        self.assertEqual('Updated', product[0].description, response.data)
        self.assertNotEqual('Updated', product[1].name, response.data)
        self.assertIsNotNone(product[0].date_updated, response.data)
        self.assertIsNone(product[1].date_updated, response.data)

    def test_update_not_exist(self):
        mommy.make('items.Item',
                   _quantity=2)
        product = {
            'name': 'Updated',
        }
        data = {'pk': 3}
        view = reverse('api:update', kwargs=data)
        response = self.client.patch(view, product, format='json')
        self.assertEqual(404, response.status_code, response.data)
