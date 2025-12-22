from recipes.tests.base_recipes_test import BaseRecipesTest
from django.urls import resolve
from recipes.views import category


class TestCategoryView(BaseRecipesTest):

    # View functions tests

    def test_category_view_function(self):
        view = resolve(self.category_url())
        assert view.func is category

    # Status Code 200 tests

    def test_category_view_returns_status_code_200_ok(self):
        category = self.get_category()
        response = self.client.get(self.category_url(id=category.id))
        assert response.status_code == 200

    # Status code 404 tests

    def test_category_view_returns_status_code_404_ok(self):
        response = self.client.get(self.category_url(id=1000))
        assert response.status_code == 404

    # Loading Correct Template Tests

    def test_category_view_loads_correct_template(self):
        category = self.get_category()
        response = self.client.get(self.category_url(id=category.id))
        self.assertTemplateUsed(
            response, 'recipes/pages/recipes-category.html')

    # Load Correct Template Content tests

    def test_category_loads_correct_template_content(self):
        recipe = self.get_recipe(
            title="Recipe Test For Category View",
            author={"first_name": "First Name Test For Category View"},
            category={'name': "Category Test For Category View"},
            description="This is a This is a description test For Category View",  # noqa E501
        )

        response = self.client.get(self.category_url(id=recipe.category.id))
        content = response.content.decode('utf-8')

        assert "Recipe Test For Category View" in content
        assert "First Name Test For Category View" in content
        assert "Category Test For Category View" in content
        assert "This is a description test For Category View" in content

    # Do not load if recipe is not published

    def test_category_view_does_not_load_not_published_recipes(self):
        recipe = self.get_recipe(is_published=False)
        response = self.client.get(self.category_url(id=recipe.category.id))
        content = response.content.decode("utf-8")

        assert f"No {recipe.category.name} Recipes Found Here" in content
