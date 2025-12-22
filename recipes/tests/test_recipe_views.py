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

    def test_home_does_not_load_not_published_recipes(self):
        recipe = self.get_recipe(is_published=False)  # noqa
        response = self.client.get(self.home_url())

        content = response.content.decode("utf-8")
        assert "No recipes found here" in content

    def test_category_view_does_not_load_not_published_recipes(self):
        recipe = self.get_recipe(is_published=False)
        response = self.client.get(self.category_url(id=recipe.category.id))
        content = response.content.decode("utf-8")

        assert f"No {recipe.category.name} Recipes Found Here" in content

    def test_recipe_view_does_not_load_not_published_recipe(self):
        recipe = self.get_recipe(is_published=False)
        response = self.client.get(self.recipe_url(id=recipe.id))

        assert response.status_code == 404
