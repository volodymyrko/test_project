"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import unittest

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class ContactTest(unittest.TestCase):
	def setUp(self):
		self.contact = Conatct.objects.create(name='name', surname='surname',
			birthday='birthday', bio='bio', contacts='contacts')


class IndexPageTest(TestCase):
	def test_index(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

