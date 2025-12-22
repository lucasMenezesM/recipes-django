from recipes.tests.base_recipes_test import BaseRecipesTest
from django.urls import resolve
from recipes.views import recipe


class TestRecipeView(BaseRecipesTest):
    # View functions tests

    def test_recipe_view_function(self):
        view = resolve(self.recipe_url())
        assert view.func == recipe

    # Status Code 200 tests

    def test_recipe_view_returns_status_code_200_ok(self):
        recipe = self.get_recipe()
        response = self.client.get(self.recipe_url(id=recipe.id))
        assert response.status_code == 200

    # Status code 404 tests

    def test_recipe_view_returns_status_code_404_ok(self):
        response = self.client.get(self.recipe_url(id=10000))
        assert response.status_code == 404

    def test_recipe_template_shows_not_found_message(self):
        response = self.client.get(self.home_url())
        content = response.content.decode('utf-8')
        assert 'No recipes found here' in content

    # Loading Correct Template Tests

    def test_recipe_view_loads_correct_template(self):
        recipe = self.get_recipe()
        response = self.client.get(self.recipe_url(id=recipe.id))
        self.assertTemplateUsed(response, 'recipes/pages/recipe-view.html')

    # Load Correct Template Content tests

    def test_recipe_loads_correct_template_content(self):
        recipe = self.get_recipe(
            title="Recipe Test For Recipe View",
            author={"first_name": "First Name Test For Recipe View"},
            category={'name': "Category Test For Recipe View"},
            description="This is a This is a description test For Recipe View"
        )

        response = self.client.get(self.recipe_url(id=recipe.id))
        content = response.content.decode('utf-8')

        assert "Recipe Test For Recipe View" in content
        assert "First Name Test For Recipe View" in content
        assert "Category Test For Recipe View" in content
        assert "This is a description test For Recipe View" in content

    # Do not load if recipe is not published

    def test_recipe_view_does_not_load_not_published_recipe(self):
        recipe = self.get_recipe(is_published=False)
        response = self.client.get(self.recipe_url(id=recipe.id))

        assert response.status_code == 404
