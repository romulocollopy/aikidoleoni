# coding: utf-8

from django.test import TestCase, Client


class TestViews(TestCase):

    """ Test Blog Views """
    def test_posts_list_view(self):
        resp = self.client.get('/publicações/')
        """ assert post status code is 200"""
        self.assertEqual(200, resp.status_code)

    def test_posts__list_template_is_used(self):
        resp = self.client.get('/publicações/')
        """ assert posts renders template """
        self.assertTemplateUsed(resp, 'blog/posts_list.html')

    def test_post_detail_view(self):
        resp = self.client.get('/publicações/belezão-aê/')
        """ assert post status code is 200"""
        self.assertEqual(200, resp.status_code)

    def test_post_detail_template_is_used(self):
        resp = self.client.get('/publicações/belezão-aê/')
        """ assert posts renders template """
        self.assertTemplateUsed(resp, 'blog/post_detail.html')
