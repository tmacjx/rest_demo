# coding=utf-8
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from requests.auth import HTTPBasicAuth, \
from rest_framework.test import APIClient


User = get_user_model()

# TODO，针对每一个action，都写一个测试用例， 如何模拟数据？模拟数据库操作？默认测试下的数据库是，单独的一个用于测试的数据库


# TODO 测试login
# 首先模拟出一个superuser
class LoginTests(APITestCase):
    # def test_login_test(self):
    #     url = reverse('account-list')
    #     data = {'name': 'DabApps'}
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Account.objects.count(), 1)
    #     self.assertEqual(Account.objects.get().name, 'DabApps')
    def setUp(self):
        User.objects.get_or_create(username='tmac', password='kk123123', is_superuser=True)
        self.login_url = reverse('login')

    def test_login(self):
        client = APIClient()
        # client = RequestsClient()
        client.auth = HTTPBasicAuth('user', 'pass')

    def test_list(self):






