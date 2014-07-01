from django.shortcuts import render
from django.core.urlresolvers import resolve
from django.test import TestCase

home_page = None

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

