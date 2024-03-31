from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


bd_pizzas = [
    {
        "id": 1,
        "name": "Маргарита",
        "ingredients": ["томатный соус", "сыр моцарелла", "базилик"],
        "price": 12,
        "is_spicy": False
    },
    {
        "id": 2,
        "name": "Пепперони",
        "ingredients": ["томатный соус", "сыр моцарелла", "пепперони", "орегано"],
        "price": 15,
        "is_spicy": True
    },
    {
        "id": 3,
        "name": "4 сыра",
        "ingredients": ["томатный соус", "сыр моцарелла", "сыр дор блю", "сыр пармезан", "сыр чеддер"],
        "price": 18,
        "is_spicy": False
    },
    {
        "id": 4,
        "name": "Гавайская",
        "ingredients": ["томатный соус", "сыр моцарелла", "ветчина", "ананасы"],
        "price": 14,
        "is_spicy": False
    },
    {
        "id": 5,
        "name": "Барбекю",
        "ingredients": ["барбекю соус", "сыр моцарелла", "курица", "лук красный", "бекон"],
        "price": 16,
        "is_spicy": False
    }
]


bd_drinks = [
    {
        "id": 1,
        "name": "Кола",
        "price": 1.5,
        "is_alcoholic": False
    },
    {
        "id": 2,
        "name": "Спрайт",
        "price": 1.5,
        "is_alcoholic": False
    },
    {
        "id": 3,
        "name": "Фанта",
        "price": 1.5,
        "is_alcoholic": False
    },
    {
        "id": 4,
        "name": "Лимонад",
        "price": 2.0,
        "is_alcoholic": False
    },
    {
        "id": 5,
        "name": "Пиво",
        "price": 2.5,
        "is_alcoholic": True
    }
]


def menu(request):
    # t = render_to_string('menu/menu.html')
    # return HttpResponse(t)
    data = {
        'title': 'Меню',
        'pizzas': bd_pizzas,
        'drinks': bd_drinks,
    }
    return render(request, 'menu/menu.html', context=data)


def pizza(request):
    if request.GET:
        print(request.GET)  # Вывод ключ значение -> http://127.0.0.1:8000/menu/pizza/?name=margarita&pizzadiameter=12
    return HttpResponse(f'<h1>Страница пиццы ')
# def pizza(request, pizza):
#     return HttpResponse(f'<h1>Страница пиццы {pizza}</h1><p>Описание пиццы {pizza}')


def drinks(request, drink):
    if drink:
        return HttpResponse(f"Страница напитка '{drink}'")
    else:
        return HttpResponse('Страница напитков')


def archive(request, year):
    if year > 2024:
        uri = reverse('home')
# Если был бы слаг, то надо было так использовать для вычисления url 'slug' or any
# path('archive/<slug:pizza>/', views.pizza)
        return HttpResponseRedirect(uri)  # -> перенаправление (redirect) для 301, для 302 HttpResponsePermanentRedirect
        # or return redirect(uri)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')
# def archive(request, year):
#     if year > 2024:
#         raise Http404()
#     return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')




