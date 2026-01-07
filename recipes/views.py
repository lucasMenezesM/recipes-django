from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category
from django.http import Http404
from django.db.models import Q
# Create your views here.


def home(request):
    recipes = Recipe.objects.filter(is_published=True)
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    recipes = Recipe.objects.filter(category=category, is_published=True)

    return render(request, 'recipes/pages/recipes-category.html', context={
        'recipes': recipes,
        'title': f"{category.name} - Categoria",
        'category_name': category.name
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id, is_published=True)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True
    })


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(title__contains=search_term) | Q(description__contains=search_term)
    ).order_by('-id')

    recipes = recipes.filter(is_published=True)

    return render(request, 'recipes/pages/search.html', context={
        "search_term": search_term,
        "recipes": recipes
    })
