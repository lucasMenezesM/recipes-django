from django.urls import resolve
from recipes import views
# from ..models import Category, Recipe, User
from .base_view_test import BaseViewTest


class RecipeViewsTest(BaseViewTest):

    # View functions tests

    def test_home_view_function(self):
        view = resolve(self.home_url())
        assert view.func is views.home

    def test_category_view_function(self):
        view = resolve(self.category_url())
        assert view.func is views.category

    def test_recipe_view_function(self):
        view = resolve(self.recipe_url())
        assert view.func == views.recipe

    # Status Code 200 tests

    def test_home_view_returns_status_code_200_ok(self):
        response = self.client.get(self.home_url())
        assert response.status_code == 200

    def test_category_view_returns_status_code_200_ok(self):
        category = self.get_category()
        response = self.client.get(self.category_url(id=category.id))
        assert response.status_code == 200

    def test_recipe_view_returns_status_code_200_ok(self):
        recipe = self.get_recipe()
        response = self.client.get(self.recipe_url(id=recipe.id))
        assert response.status_code == 200

    # Status code 404 tests

    def test_category_view_returns_status_code_404_ok(self):
        response = self.client.get(self.category_url(id=1000))
        assert response.status_code == 404

    def test_recipe_view_returns_status_code_404_ok(self):
        response = self.client.get(self.recipe_url(id=10000))
        assert response.status_code == 404

    def test_recipe_template_shows_not_found_message(self):
        response = self.client.get(self.home_url())
        content = response.content.decode('utf-8')
        assert 'No recipes found here' in content

    # Loading Correct Template Tests

    def test_home_view_loads_correct_template(self):
        response = self.client.get(self.home_url())
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_view_loads_correct_template(self):
        recipe = self.get_recipe()
        response = self.client.get(self.recipe_url(id=recipe.id))
        self.assertTemplateUsed(response, 'recipes/pages/recipe-view.html')

    def test_category_view_loads_correct_template(self):
        category = self.get_category()
        response = self.client.get(self.category_url(id=category.id))
        self.assertTemplateUsed(
            response, 'recipes/pages/recipes-category.html')
