
from django.urls import reverse
from ..models import Category, Recipe, User

# Util Functions


def home_url():
    return reverse('recipes:home')


def category_url(id: int = 1):
    return reverse('recipes:category',  kwargs={'category_id': id})


def recipe_url(id: int = 1):
    return reverse('recipes:recipe', kwargs={'id': id})


def get_category():
    return Category.objects.create(name='Category 1')


def get_user():
    return User.objects.create_user(
        first_name='User',
        last_name='User',
        username='username',
        email='username@email.com',
        password='123456',
    )


def get_recipe():
    category = get_category()
    author = get_user()

    return Recipe.objects.create(
        title='Recipe',
        description='Pretty good Recipe',
        slug='recipe-recipe',
        preparation_time=2,
        preparation_time_unit='minutes',
        servings=2,
        servings_unit='people',
        preparation_steps=2,
        preparation_steps_is_html=True,
        category=category,
        author=author,
        is_published=True
    )
