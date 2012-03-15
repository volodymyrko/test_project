"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import unittest

from http_middleware.models import HttpRequestStore
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class HttpReqeustTest(unittest.TestCase):
    def setUp(self):
        self.path='/'
        self.record = HttpRequestStore.objects.create(path=self.path,
            method='GET', remote_address='127.0.0.1')

    def test_http_middleware(self):
        """ Test for request saving
        """
        self.assertTrue(HttpRequestStore.objects.filter(path=self.path).count() > 0)
