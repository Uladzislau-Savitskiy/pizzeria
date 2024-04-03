from django.http import HttpResponse
from django.shortcuts import render


menu = [
    {
        'title': 'Меню',
        'url_name': 'menu',
     },
    {
        'title': 'Отзывы',
        'url_name': 'reviews',
     },
    {
        'title': 'Доставка',
        'url_name': 'delivery',
     },
    {
        'title': 'О нас',
        'url_name': 'about',
     },
    {
        'title': 'Корзина',
        'url_name': 'order_cart',
     },
    {
        'title': 'Войти',
        'url_name': 'login',
     },
]


def homepage(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'balance': 500.45,
        'news': ['Новость дня 1', 'Новость дня 2', 'Новость дня 3'],

    }
    return render(request, 'homepage/homepage.html', context=data)


def about(request):
    return render(request, 'homepage/about.html', {'title': 'О нас', 'menu': menu})


def login(request):
    return render(request, 'homepage/login.html', {'title': 'Вход', 'menu': menu})


def order_cart(request):
    return render(request, 'homepage/order_cart.html', {'title': 'Корзина', 'menu': menu})
