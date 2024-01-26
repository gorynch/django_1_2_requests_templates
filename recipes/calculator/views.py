from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def index(request):
    context = {
        'names': list(DATA.keys())
    }
    return render(request, 'index.html', context)


def omlet(request):
    count = int(request.GET.get('servings', 1))
    if count > 1:
        for k, v in DATA['omlet'].items():
            DATA['pasta'][k] = v*count
    context = {
        'recipe': DATA['omlet'],
        "count": count,
        'name': 'omlet'
    }
    return render(request, 'recipe.html', context)


def pasta(request):
    count = int(request.GET.get('servings', 1))
    if count > 1:
        for k, v in DATA['pasta'].items():
            DATA['pasta'][k] = v*count
    context = {
        'recipe': DATA['pasta'],
        "count": count,
        'name': 'pasta'
    }
    return render(request, 'recipe.html', context)


def buter(request):
    count = int(request.GET.get('servings', 1))
    if count > 1:
        for k, v in DATA['buter'].items():
            DATA['pasta'][k] = v*count
    context = {
        'recipe': DATA['buter'],
        "count": count,
        'name': 'buter'
    }
    return render(request, 'recipe.html', context)


def recipe(request, dish):
    count = int(request.GET.get('servings', 1))
    context = {}
    if dish in DATA:
        context = DATA[dish]
    return render(request, 'index.html', context)
    # return HttpResponse(f"omlet for {count} person(s)")
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
