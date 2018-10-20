from django.urls import reverse
from rest_framework.test import APITestCase
from model_mommy import mommy
from items.models import Item


class ProductsDeleteAPITest(APITestCase):
    def setUp(self):
        super().setUp()

    def test_delete_product(self):

        seller = mommy.make('sellers.Seller',
                            name='TestSeller')
        mommy.make('items.Item',
                   seller=seller,
                   _quantity=2)

        data = {'pk': 1}

        view = reverse('api:delete', kwargs=data)

        response = self.client.delete(view, format='json')
        self.assertEqual(204, response.status_code, response.data)
        product_count = Item.objects.count()
        self.assertEqual(1, product_count, response.data)

    def test_delete_not_exist(self):
        seller = mommy.make('sellers.Seller',
                            name='TestSeller')
        mommy.make('items.Item',
                   seller=seller,
                   _quantity=1)

        data = {'pk': 2}

        view = reverse('api:delete', kwargs=data)

        response = self.client.delete(view, format='json')
        self.assertEqual(404, response.status_code, response.data)
        product_count = Item.objects.count()
        self.assertEqual(1, product_count, response.data)
