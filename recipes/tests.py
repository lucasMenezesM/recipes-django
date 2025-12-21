from django.test import TestCase

# Create your tests here.


class RecipeURLsTest(TestCase):
    def test_the_pytest_is_ok(self):
        print("Hello world from pytest")
        name: str = 'pytest variable'
        print(name)
        assert 1 == 1, '1 é igual a 1'
