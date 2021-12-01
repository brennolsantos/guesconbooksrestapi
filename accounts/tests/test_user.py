from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse

# Test


class UserTest(APITestCase):

    def test_usertest(self):
        """
        This test creates ten users and
        check queryset User's len
        """

        users = get_user_model()

        for i in range(1, 11):
            response = self.client.post(reverse('accounts:register-list'), {
                'username': 'test' + str(i),
                'password': '@Test12345678',
                'password2': '@Test12345678',
                'email': 'test' + str(i) + '@test.com',
                'name': 'John Dove'
            }, format='json')

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(users.objects.count(), 10)
