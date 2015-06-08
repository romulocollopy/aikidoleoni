# coding: utf-8

from django.test import TestCase
from model_mommy import mommy

from aikidoleoni.core.models import Page


class TestUrls(TestCase):

    """ Test Blog Views """

    def setUp(self):
        mommy.make(Page, slug="blog")

    def test_posts_list_view(self):
        """ assert post status code is 200"""
        resp = self.client.get('/publicações/')
        self.assertEqual(200, resp.status_code)

    def test_posts__list_template_is_used(self):
        """ assert posts renders template """
        resp = self.client.get('/publicações/')
        self.assertTemplateUsed(resp, 'blog/posts_list.html')

    def test_post_detail_view(self):
        """ assert post status code is 200"""
        resp = self.client.get('/publicações/belezão-aê/')
        self.assertEqual(200, resp.status_code)

    def test_post_detail_template_is_used(self):
        """ assert posts renders template """
        resp = self.client.get('/publicações/belezão-aê/')
        self.assertTemplateUsed(resp, 'blog/post_detail.html')
