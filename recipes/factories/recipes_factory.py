import factory
from recipes.models import Recipe
from .category_factory import CategoryFactory
from .users_factory import UserFactory
import random


class RecipeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Recipe

    title = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('paragraph')
    preparation_time = factory.Faker('random_int', min=10, max=120)
    # slug = "-".join(title.split())
    slug = title
    preparation_time_unit = random.choice(["Minutes", "Hours"])
    servings = factory.Faker("random_int", min=1, max=20)
    preparation_steps = factory.Faker('paragraph')
    is_published = random.choice([True, False])
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
