from django.http import HttpResponse
from django.shortcuts import render


catalogs = ['Меню', 'Отзывы', 'Доставка', 'О нас', 'Войти']
# Create your views here.


def homepage(request):
    data = {
        'title': 'Главная страница',
        'catalogs': catalogs,
        'balance': 500.45,
        'news': ['Новость дня 1', 'Новость дня 2', 'Новость дня 3'],

    }
    return render(request, 'homepage/homepage.html', context=data)


def about(request):
    return render(request, 'homepage/about.html', {'title': 'О нас'})
