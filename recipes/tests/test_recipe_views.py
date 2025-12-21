from django.test import TestCase
from django.urls import reverse, resolve
from .. import views


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
