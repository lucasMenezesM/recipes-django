from django.test import TestCase
from django.urls import resolve
from recipes import views
# from ..models import Category, Recipe, User
from .utils import get_category, get_recipe, home_url, category_url, recipe_url


class RecipeViewsTest(TestCase):

    # View functions tests

    def test_home_view_function(self):
        view = resolve(home_url())
        assert view.func is views.home

    def test_category_view_function(self):
        view = resolve(category_url())
        assert view.func is views.category

    def test_recipe_view_function(self):
        view = resolve(recipe_url())
        assert view.func == views.recipe

    # Status Code 200 tests

    def test_home_view_returns_status_code_200_ok(self):
        response = self.client.get(home_url())
        assert response.status_code == 200

    def test_category_view_returns_status_code_200_ok(self):
        category = get_category()
        response = self.client.get(category_url(id=category.id))
        assert response.status_code == 200

    def test_recipe_view_returns_status_code_200_ok(self):
        recipe = get_recipe()
        response = self.client.get(recipe_url(id=recipe.id))
        assert response.status_code == 200

    # Status code 404 tests

    def test_category_view_returns_status_code_404_ok(self):
        response = self.client.get(category_url(id=1000))
        assert response.status_code == 404

    def test_recipe_view_returns_status_code_404_ok(self):
        response = self.client.get(recipe_url(id=10000))
        assert response.status_code == 404

    def test_recipe_template_shows_not_found_message(self):
        response = self.client.get(home_url())
        content = response.content.decode('utf-8')
        assert 'No recipes found here' in content

    # Templates tests

    def test_home_view_loads_correct_template(self):
        response = self.client.get(home_url())
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_view_loads_correct_template(self):
        recipe = get_recipe()
        response = self.client.get(recipe_url(id=recipe.id))
        self.assertTemplateUsed(response, 'recipes/pages/recipe-view.html')

    def test_category_view_loads_correct_template(self):
        category = get_category()
        response = self.client.get(category_url(id=category.id))
        self.assertTemplateUsed(
            response, 'recipes/pages/recipes-category.html')
