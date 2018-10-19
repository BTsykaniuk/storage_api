from django.urls import reverse
from rest_framework.test import APITestCase
from model_mommy import mommy


class ProductsCreateAPITest(APITestCase):
    def setUp(self):
        super().setUp()
        self.view = reverse('api:list')

    def test_list_items(self):
        """
        Test bulk create
        """
        seller = mommy.make('sellers.Seller',
                            name='TestSeller')
        mommy.make('items.Item',
                   seller=seller,
                   _quantity=5)

        response = self.client.get(self.view, format='json')
        self.assertEqual(200, response.status_code, response.data)
        self.assertEqual(5, len(response.data['results']), response.data['results'])
