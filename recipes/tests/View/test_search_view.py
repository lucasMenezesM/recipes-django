from recipes.tests.base_recipes_test import BaseRecipesTest
from django.urls import resolve
from recipes.views import search


class TestRecipeView(BaseRecipesTest):
    def test_search_view_is_correct(self):
        view = resolve(self.search_url())

        assert view.func == search

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(self.search_url())
        self.assertTemplateUsed(response, 'recipes/pages/search.html')
