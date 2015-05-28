# coding: utf-8

from django.test import TestCase, Client
from django.db.models.query import QuerySet

from model_mommy import mommy

from aikidoleoni.core.models import Page
from aikidoleoni.blog.models import Post


class TestViews(TestCase):

    """ Test Blog Views """

    def setUp(self):
        mommy.make(Page, slug="blog")

    def test_posts_list_view(self):
        """ assert post status code is 200"""
        resp = self.client.get('/publicações/')
        page = resp.context['page']
        self.assertIsInstance(page, Page)

    def test_post_detail_view(self):
        """ assert post status code is 200"""
        resp = self.client.get('/publicações/belezão-aê/')
        page = resp.context['page']
        self.assertIsInstance(page, Page)

    def test_page_has_post_queryset(self):
        """ assert page has a post queryset """
        resp = self.client.get('/publicações/')
        posts = resp.context['posts']
        self.assertEqual(QuerySet, type(posts))

    def test_asser_posts_in_queryset(self):
        mommy.make(Post)
        resp = self.client.get('/publicações/')
        post = resp.context['posts'][0]
        self.assertIsInstance(post, Post)
