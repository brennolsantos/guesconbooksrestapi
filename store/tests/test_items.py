from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from rest_framework.reverse import reverse
from rest_framework import status
from store.models import Book, Magazine, Author, Genre, Company
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from model_mommy import mommy

User = get_user_model()


class ItemTests(APITestCase):
    """
    This test class tests the creation
    of books and magazines
    """

    def setUp(self):

        self.NAME = 'John Dove'
        self.PASSWORD = '@Test12345678'

        self.companies = mommy.make(
            Company, update_date=timezone.now(), _quantity=2)
        self.authors = mommy.make(
            Author, _quantity=2)
        self.genres = mommy.make(
            Genre, _quantity=2)

    def tearDown(self):
        pass

    def test_books_creation(self):
        user = User.objects.create_superuser(
            username='test', email='test@test.com', password=self.PASSWORD)

        self.client.force_authenticate(user=user)

        self.assertEqual(Company.objects.all().count(), 2)
        self.assertEqual(Author.objects.all().count(), 2)
        self.assertEqual(Genre.objects.all().count(), 2)

        date = timezone.now()

        a = get_object_or_404(Author, pk=1)
        g = get_object_or_404(Genre, pk=1)
        c = get_object_or_404(Company, pk=1)

        response = self.client.post(reverse('store:create-book'), data={
            'author': a.pk,
            'company': c.pk,
            'genre': g.pk,
            'title': 'Book',
            'desc': 'Book',
            'num_pages': 123,
            'price': '44.55',
            'cover': None,
            'publish_date': date.strftime("%Y-%m-%dT%H:%M:%SZ")
        }, format='json')

        self.assertEqual(Book.objects.all().count(), 1)

        self.client.logout()
        user.delete()




    def test_magazines_creation(self):
        user = User.objects.create_superuser(
            username='test2', email='test2@test.com', password=self.PASSWORD)

        self.client.login(username='test2', password=self.PASSWORD)

        self.assertEqual(Company.objects.all().count(), 2)
        self.assertEqual(Author.objects.all().count(), 2)
        self.assertEqual(Genre.objects.all().count(), 2)

        date = timezone.now()
        g = get_object_or_404(Genre, pk=2)
        c = get_object_or_404(Company, pk=2)

        response = self.client.post(reverse('store:create-magazine'), data={
            'company': c.pk,
            'genre': g.pk,
            'title': 'Magazine',
            'desc': 'Magazine',
            'num_pages': 123,
            'price': '44.55',
            'edition': 10,
            'cover': None,
            'publish_date': date.strftime("%Y-%m-%dT%H:%M:%SZ")
        }, format='json')

        self.assertEqual(Magazine.objects.all().count(), 1)


        self.client.logout()
