from recipes.tests.base_recipes_test import BaseRecipesTest
import pytest
from django.core.exceptions import ValidationError


class TestCategoryModel(BaseRecipesTest):
    def setUp(self):
        self.category = self.get_category(name="Category Test")
        return super().setUp()

    def test_name_max_length(self):
        self.category.name = "A" * 70
        with pytest.raises(ValidationError):
            self.category.full_clean()

    def test_recipe_string_name_representation(self):

        assert str(self.category) == self.category.name
