from recipes.tests.base_recipes_test import BaseRecipesTest
from django.urls import resolve
from recipes.views import search


class TestRecipeView(BaseRecipesTest):
    def test_search_view_is_correct(self):
        view = resolve(self.search_url())

        assert view.func == search

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(self.search_url() + "?q=test")
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raises_404_if_no_search_term(self):
        response = self.client.get(self.search_url())

        assert response.status_code == 404

    def test_recipe_search_term_is_on_page(self):
        response = self.client.get(self.search_url() + "?q=test")
        content = response.content.decode('utf-8')

        assert 'Searching for "test"' in content
