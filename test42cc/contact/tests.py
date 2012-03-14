"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import unittest
from contact.models import Contact

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class IndexPageTest(TestCase):
    def test_index(self):
        """Test for http request main page
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class ContactTest(unittest.TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(name='name', surname='surname',
            birthday='birthday', bio='bio', email='email@server.ua', jabber='jabber@server.com',
            skype='skype_name', contacts='contacts')

    def test_entry_exists(self):
        """ Test for Contact object creation
        """
        self.assertNotEqual(Contact.objects.count(), 0)