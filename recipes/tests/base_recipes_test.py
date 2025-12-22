
from django.urls import reverse
from ..models import Category, Recipe, User
from django.test import TestCase


class BaseRecipesTest(TestCase):

    def setUp(self):
        return super().setUp()

    def home_url(self):
        return reverse('recipes:home')

    def category_url(self, id: int = 1):
        return reverse('recipes:category',  kwargs={'category_id': id})

    def recipe_url(self, id: int = 1):
        return reverse('recipes:recipe', kwargs={'id': id})

    def get_category(self, name='Category 1'):
        return Category.objects.create(name=name)

    def get_user(self, first_name='User',
                 last_name='User',
                 username='username',
                 email='username@email.com',
                 password='123456',
                 ):

        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )

    def get_recipe(self, title='Recipe',
                   description='Pretty good Recipe',
                   slug='recipe-recipe',
                   preparation_time=2,
                   preparation_time_unit='minutes',
                   servings=2,
                   servings_unit='people',
                   preparation_steps=2,
                   preparation_steps_is_html=True,
                   category=None,
                   author=None,
                   is_published=True
                   ):

        if category is None:
            category = {}
        if author is None:
            author = {}

        return Recipe.objects.create(
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            category=self.get_category(**category),
            author=self.get_user(**author),
            is_published=is_published
        )
