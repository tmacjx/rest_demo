# coding=utf-8
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from rest_framework.test import APITestCase

# TODO，针对每一个action，都写一个测试用例， 如何模拟数据？模拟数据库操作？默认测试下的数据库是，单独的一个用于测试的数据库


# TODO 测试login
# 首先模拟出一个superuser
class UserTest(APITestCase):

    def test_sign(self):
        pass

    def test_signup(self):
        pass

    def test_testlogin(self):
        pass