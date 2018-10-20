from django.urls import reverse
from rest_framework.test import APITestCase
from model_mommy import mommy


class SellersListAPITest(APITestCase):
    def setUp(self):
        super().setUp()
        self.view = reverse('api:sellers')

    def test_sellers_list(self):
        sellers = mommy.make('sellers.Seller',
                             _quantity=2)
        mommy.make('items.Item',
                   seller=sellers[0],
                   _quantity=5)

        mommy.make('items.Item',
                   seller=sellers[1],
                   _quantity=5)

        response = self.client.get(self.view, format='json')
        self.assertEqual(200, response.status_code, response.data)
        self.assertEqual(2, len(response.data['results']), response.data)
        self.assertEqual(5, len(response.data['results'][0]['items']), response.data)
