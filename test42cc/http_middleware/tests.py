"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import unittest
from django.test.client import Client
from django.core.urlresolvers import reverse
from http_middleware.models import HttpRequestStore

TOO_HIGHT_GET_PARAM = '99999999'
BAD_GET_PARAM = 'not_integer'

class HttpReqeustTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.path = '/'
        self.record = HttpRequestStore.objects.create(path=self.path,
            method='GET', remote_address='127.0.0.1')

    def test_http_middleware(self):
        """ Test for request saving in db
        """
        count = HttpRequestStore.objects.filter(path=self.path).count()
        self.assertTrue( count > 0)

    def test_get_response(self):
        """ testing  get '/requests/' result
        """
        url = reverse('requests')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        url = reverse('requests')
        response = self.client.get(url, {'page': TOO_HIGHT_GET_PARAM})
        self.assertEqual(response.status_code, 200)

        url = reverse('requests')
        response = self.client.get(url, {'page': BAD_GET_PARAM })
        self.assertEqual(response.status_code, 200)
