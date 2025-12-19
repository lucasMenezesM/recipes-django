from django.shortcuts import render
from .models import Recipe
# Create your views here.


def home(request):
    recipes = Recipe.objects.filter(is_published=True)
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(category_id=category_id, is_published=True)
    return render(request, 'recipes/pages/home.html', context = {
        'recipes': recipes
    })


def recipe(request, id):
    recipe_item = Recipe.objects.filter(id=id, is_published=True).first()
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe_item,
        'is_detail_page': True
    })

