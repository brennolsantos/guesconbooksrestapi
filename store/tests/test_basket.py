from datetime import timezone
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from store.models import Book, Magazine, Basket, BasketItem, Genre, Author, Company
from django.contrib.auth import get_user_model
from model_mommy import mommy
from django.utils import timezone

User = get_user_model()


class BasketTests(APITestCase):

    """
    This tests compares the len of Basket when ships 
    Books and Magazines
    """

    def setUp(self):
        m_company = mommy.make(Company)
        m_author = mommy.make(Author)
        m_genre = mommy.make(Genre)
        m_book = mommy.make(Book, price=10.00, _quantity=10)
        m_magazine = mommy.make(Magazine, price=10.00,  _quantity=10)

        self.books = Book.objects.all()
        self.magazines = Magazine.objects.all()
        self.PASSWORD = '@Test12345678'

        self.user = User.objects.create_user(username='test', password=self.PASSWORD)

    
    def tearDown(self):
        pass

    def test_books_ship(self):

        self.client.force_authenticate(user=self.user)

        for i in range(1,11):
            response = self.client.post(reverse('store:buy-item'), data={
                'type': 'b',
                'id': i
            }, format='json')

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Basket.objects.all().count(), 1)
        self.assertEqual(BasketItem.objects.all().count(), 10)

        self.client.logout()


    def test_magazines_ship(self):
        
        self.client.force_authenticate(user=self.user)

        for i in range(1,11):
            response = self.client.post(reverse('store:buy-item'), data={
                'type': 'm',
                'id': i
            }, format='json')

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Basket.objects.all().count(), 1)
        self.assertEqual(BasketItem.objects.all().count(), 10)
