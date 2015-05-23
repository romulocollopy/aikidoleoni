# coding: utf-8

from django.test import TestCase, Client


class TestViews(TestCase):

    """ Test Core Views """

    def setUp(self):
        self.resp = self.client.get('/')

    def test_home_view(self):
        """ assert home status code is 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_home_template_is_used(self):
        """ assert home renders template """
        self.assertTemplateUsed(self.resp, 'core/home.html')