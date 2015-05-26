# coding: utf-8

from django.test import TestCase
from aikidoleoni.core.models import Page
from django.db.utils import IntegrityError
from model_mommy import mommy


class TestModels(TestCase):
    """ Test Core Models """

    def test_pagina_model(self):
        """ assert page is created """
        mommy.make(Page, id=16)
        page = Page.objects.get()
        self.assertEqual(16, page.id)

    def test_pagina_slug_is_unique(self):
        """ assert page is created """
        mommy.make(Page, slug='home')
        self.assertRaises(IntegrityError, mommy.make, Page, slug='home')
