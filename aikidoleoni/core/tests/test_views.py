# coding: utf-8

from django.test import TestCase, Client
from model_mommy import mommy

from aikidoleoni.core.models import Page
from aikidoleoni.blog.models import Post

class TestHomeView(TestCase):
    """ Test Core Views """
    def setUp(self):
        mommy.make('Page', slug='home')
        mommy.make('Page', slug='contato')
        mommy.make('Page', slug='sobre')
        mommy.make('Page', slug='sobre-o-aikido')
        self.resp = self.client.get('/')

    def test_home_has_page_instance(self):
        """ Tests if Home has one instance of Page """
        page = self.resp.context['page']
        self.assertIsInstance(page, Page)

    def test_home_page_instace_has_slug_home(self):
        """ Test page instance from home has 'home' slug """
        page = self.resp.context['page']
        self.assertEqual('home', page.slug)

    def test_home_page_has_fields(self):
        """ Test page instance from home has required fields """
        page = self.resp.context['page']
        self.assertIsNotNone(page.title)
        self.assertIsNotNone(page.description)
        self.assertIsNotNone(page.content)
        self.assertIsNotNone(page.image)

    def test_home_has_list_of_3_last_posts(self):
        posts = self.resp.context['posts']
        self.assertEqual(3, len(posts))

    def test_home_has_list_posts_has_instaces_of_post(self):
        post = self.resp.context['posts'][0]
        self.assertIsInstance(post, Post)

    def raises_404_if_page_does_not_exist(self):
        Page.objects.get('home').delete()
        resp = self.client.get('/')
        self.assertEqual(404, resp.status_code)



class TestAboutView(TestCase):
    """ Test About Views """
    def setUp(self):
        mommy.make('Page', slug='home')
        mommy.make('Page', slug='contato')
        mommy.make('Page', slug='sobre')
        mommy.make('Page', slug='sobre-o-aikido')
        self.resp = self.client.get('/sobre/')

    def test_about_has_page_instance(self):
        """ Tests if About has one instance of Page """
        page = self.resp.context['page']
        self.assertIsInstance(page, Page)

    def test_home_page_instace_has_slug_sobre(self):
        """ Test page instance from home has 'sobre' slug """
        page = self.resp.context['page']
        self.assertEqual('sobre', page.slug)

    def test_about_page_has_fields(self):
        """ Test page instance from home has required fields """
        page = self.resp.context['page']
        self.assertIsNotNone(page.title)
        self.assertIsNotNone(page.description)
        self.assertIsNotNone(page.content)
        self.assertIsNotNone(page.image)

class TestAboutAikido(TestCase):
    """ Test About Aikido View """
    def setUp(self):
        mommy.make('Page', slug='home')
        mommy.make('Page', slug='contato')
        mommy.make('Page', slug='sobre')
        mommy.make('Page', slug='sobre-o-aikido')
        self.resp = self.client.get('/sobre-o-aikido/')

    def test_about_aikido_has_page_instance(self):
        """ Tests if about-aikido has one instance of Page """
        page = self.resp.context['page']
        self.assertIsInstance(page, Page)

    def test_about_aikido_page_instace_has_slug_sobre_o_aikido(self):
        """ Test page instance from home has 'sobre-o-aikido' slug """
        page = self.resp.context['page']
        self.assertEqual('sobre-o-aikido', page.slug)

    def test_about_aikido_page_has_fields(self):
        """ Test page instance from home has required fields """
        page = self.resp.context['page']
        self.assertIsNotNone(page.title)
        self.assertIsNotNone(page.description)
        self.assertIsNotNone(page.content)
        self.assertIsNotNone(page.image)

class TestContact(TestCase):
    """ Test About Aikido View """
    def setUp(self):
        mommy.make('Page', slug='home')
        mommy.make('Page', slug='contato')
        mommy.make('Page', slug='sobre')
        mommy.make('Page', slug='sobre-o-aikido')
        self.resp = self.client.get('/contato/')

    def test_contact_has_page_instance(self):
        """ Tests if contact has one instance of Page """
        page = self.resp.context['page']
        self.assertIsInstance(page, Page)

    def test_contact_page_instace_has_slug_contato(self):
        """ Test page instance from home has 'contato' slug """
        page = self.resp.context['page']
        self.assertEqual('contato', page.slug)

    def test_contact_page_has_fields(self):
        """ Test page instance from home has required fields """
        page = self.resp.context['page']
        self.assertIsNotNone(page.title)
        self.assertIsNotNone(page.description)
        self.assertIsNotNone(page.content)
        self.assertIsNotNone(page.image)

    # def test_contact_contains_csrf(self):
    #     '''Html must contain csrf token.'''
    #     self.assertContains(self.resp, 'csrfmiddlewaretoken')

