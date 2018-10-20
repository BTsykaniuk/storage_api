from django.urls import reverse
from rest_framework.test import APITestCase
from model_mommy import mommy
from items.models import Item


class ProductsCreateAPITest(APITestCase):
    def setUp(self):
        super().setUp()
        self.view = reverse('api:create')

    def test_create_product(self):
        """
        Test bulk create
        """
        seller = mommy.make('sellers.Seller',
                            name='TestSeller')
        product = {
            'name': 'some name',
            'description': 'some text',
            'seller': seller.id
        }

        response = self.client.post(self.view, product, format='json')
        self.assertEqual(201, response.status_code, response.data)
        product_count = Item.objects.count()
        self.assertEqual(1, product_count, response.data)
