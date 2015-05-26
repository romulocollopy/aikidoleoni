# coding: utf-8

from django.test import TestCase, Client


class TestUrls(TestCase):

    """ Test Core Urls """

    def setUp(self):
        self.resp = self.client.get('/')

    def test_home_view(self):
        """ assert home status code is 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_home_template_is_used(self):
        """ assert home renders template """
        self.assertTemplateUsed(self.resp, 'core/home.html')

    def test_contact_view(self):
        resp = self.client.get('/contato/')
        """ assert contact status code is 200"""
        self.assertEqual(200, resp.status_code)

    def test_contact_template_is_used(self):
        resp = self.client.get('/contato/')
        """ assert contato renders template """
        self.assertTemplateUsed(resp, 'core/contact.html')

    def test_about_view(self):
        resp = self.client.get('/sobre/')
        """ assert about status code is 200"""
        self.assertEqual(200, resp.status_code)

    def test_about_template_is_used(self):
        resp = self.client.get('/sobre/')
        """ assert sobre renders template """
        self.assertTemplateUsed(resp, 'core/about.html')

    def test_about_aikido_view(self):
        resp = self.client.get('/sobre-o-aikido/')
        """ assert about_aikido status code is 200"""
        self.assertEqual(200, resp.status_code)

    def test_about_template_is_used(self):
        resp = self.client.get('/sobre/')
        """ assert about_aikido renders template """
        self.assertTemplateUsed(resp, 'core/about.html')
