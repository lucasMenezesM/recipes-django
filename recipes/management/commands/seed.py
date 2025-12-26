from django.core.management.base import BaseCommand
from recipes.factories.category_factory import CategoryFactory
from recipes.factories.users_factory import UserFactory
from recipes.factories.recipes_factory import RecipeFactory
import random
from recipes.models import Recipe, Category
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Generates dummy data for the application"

    def add_arguments(self, parser):
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete existing data before seeding',
        )

    def handle(self, *args, **options):
        if options['delete']:
            self.stdout.write("Deleting old data...")
            Recipe.objects.all().delete()
            Category.objects.all().delete()
            User.objects.filter(is_superuser=False).delete()

        self.stdout.write("Generating data...")

        # Create 5 users
        users = UserFactory.create_batch(5)

        # Create 3 categories
        categories = CategoryFactory.create_batch(5)

        # Create 20 recipes distributed randomly among users and categories
        for _ in range(20):
            RecipeFactory.create(
                author=random.choice(users),
                category=random.choice(categories)
            )

        self.stdout.write(self.style.SUCCESS('Success: Database populated!'))
