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
    }
# можете добавить свои рецепты ;)
}


def recipe_view(request, dish):
    recipe = DATA.get(dish)
    servings = request.GET.get('servings', None)
    if recipe:
        if servings:
            context = {
                'recipe': {key: value*(int(servings) if servings is not None else 1) for key, value in recipe.items()}
            }
        else:
            context = {
                'recipe': {key: value for key, value in recipe.items()}
            }
    else:
        context = {
            'recipe': {dish: 'Нет такого рецепта'}
        }
    return render(request, 'calculator/index.html', context)


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
