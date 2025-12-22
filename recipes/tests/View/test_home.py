from recipes.tests.base_recipes_test import BaseRecipesTest
from django.urls import resolve
from recipes.views import home


class TestHomeView(BaseRecipesTest):

    # View functions tests

    def test_home_view_function(self):
        view = resolve(self.home_url())
        assert view.func is home

    # Status Code 200 tests

    def test_home_view_returns_status_code_200_ok(self):
        response = self.client.get(self.home_url())
        assert response.status_code == 200

    # Loading Correct Template Tests

    def test_home_view_loads_correct_template(self):
        response = self.client.get(self.home_url())
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    # Load Correct Template Content tests

    def test_home_loads_correct_template_content(self):
        recipe = self.get_recipe(  # noqa
            title="Recipe Test", author={"first_name": "First Name Test"},
            category={'name': "Category Test"},
            description="This is a This is a description test"
        )

        response = self.client.get(self.home_url())
        content = response.content.decode('utf-8')

        assert "Recipe Test" in content
        assert "First Name Test" in content
        assert "Category Test" in content
        assert "This is a description test" in content

    # Do not load if recipe is not published

    def test_home_does_not_load_not_published_recipes(self):
        recipe = self.get_recipe(is_published=False)  # noqa
        response = self.client.get(self.home_url())

        content = response.content.decode("utf-8")
        assert "No recipes found here" in content
