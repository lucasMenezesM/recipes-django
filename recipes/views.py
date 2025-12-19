from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe
from .models import User, Recipe, Category
# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': Recipe.objects.all()
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': Recipe.objects.filter(id=id).first(),
        'is_detail_page': True
    })