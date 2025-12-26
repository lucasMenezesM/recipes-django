from recipes.tests.base_recipes_test import BaseRecipesTest
from django.core.exceptions import ValidationError
import pytest
from parameterized import parameterized


class TestRecipeModel(BaseRecipesTest):
    def setUp(self):
        self.recipe = self.get_recipe()
        return super().setUp()

    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
    ])
    def test_max_length(self, field, max_length):
        setattr(self.recipe, field, 'a' * (max_length + 1))
        with pytest.raises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_string_name_representation(self):

        assert str(
            self.recipe) == f"{self.recipe.title} | {self.recipe.category.name}"  # noqa
