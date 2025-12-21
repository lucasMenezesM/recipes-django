from django.test import TestCase
from django.urls import reverse, resolve
from . import views

# Create your tests here.


class RecipeURLsTest(TestCase):

    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        assert url == '/'

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        assert url == '/recipes/categories/1/'

    def test_recipe_details_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        assert url == '/recipes/1/'


class RecipeViewsTest(TestCase):

    def test_home_view_function(self):
        url = reverse('recipes:home')
        view = resolve(url)
        assert view.func is views.home

    def test_category_view_function(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        view = resolve(url)
        assert view.func is views.category

    def test_recipe_view_function(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        view = resolve(url)
        assert view.func == views.recipe
