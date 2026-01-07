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

    def test_recipe_does_not_show_if_its_not_published(self):
        title = "Test if the recipe will not show"

        recipe = self.get_recipe(title=title, is_published=False)  # noqa

        response = self.client.get(self.search_url() + f"?q={title}")
        content = response.content.decode("utf-8")

        # assert title not in content
        assert "No recipes Found Here" in content

    def test_search_can_find_recipe_by_title(self):
        title1 = "this is the recipe search test 1"
        title2 = "this is the recipe search test 2"

        recipe1 = self.get_recipe(title=title1, author={"username": "user1"})
        recipe2 = self.get_recipe(title=title2, author={"username": "user2"})

        search_url = self.search_url()
        response1 = self.client.get(f"{search_url}?q={title1}")
        response2 = self.client.get(f"{search_url}?q={title2}")
        both_responses = self.client.get(
            f"{search_url}?q=this is the recipe search test")

        assert recipe1 in response1.context['recipes']
        assert recipe2 in response2.context['recipes']

        assert recipe1 not in response2.context['recipes']
        assert recipe2 not in response1.context['recipes']

        assert recipe1 in both_responses.context['recipes']
        assert recipe2 in both_responses.context['recipes']

    def test_search_can_find_by_description(self):
        description1 = "this is the recipe description search test 1"
        description2 = "this is the recipe description search test 2"

        recipe1 = self.get_recipe(
            description=description1, author={"username": "user1"})
        recipe2 = self.get_recipe(
            description=description2, author={"username": "user2"})

        search_url = self.search_url()
        response1 = self.client.get(f"{search_url}?q={description1}")
        response2 = self.client.get(f"{search_url}?q={description2}")
        both_responses = self.client.get(
            f"{search_url}?q=this is the recipe description search test")

        assert recipe1 in response1.context['recipes']
        assert recipe1.title in response1.content.decode("utf-8")
        assert recipe1 not in response2.context['recipes']

        assert recipe2 in response2.context['recipes']
        assert recipe2.title in response2.content.decode("utf-8")
        assert recipe2 not in response1.context['recipes']

        assert recipe1 in both_responses.context['recipes']
        assert recipe2 in both_responses.context['recipes']
        assert recipe1.title in both_responses.content.decode("utf-8")
        assert recipe2.title in both_responses.content.decode("utf-8")

    def test_search_can_find_recipe_by_both_description_and_title(self):
        search_term = "this is the recipe title and description search test"

        recipe1 = self.get_recipe(
            description=search_term, author={"username": "user1"})
        recipe2 = self.get_recipe(
            title=search_term, author={"username": "user2"})

        search_url = self.search_url()
        response = self.client.get(f"{search_url}?q={search_term}")

        assert recipe1 in response.context["recipes"]
        assert recipe2 in response.context["recipes"]

        assert recipe1.title in response.content.decode("utf-8")
        assert recipe2.title in response.content.decode("utf-8")

        assert recipe1.description in response.content.decode("utf-8")
        assert recipe2.description in response.content.decode("utf-8")
