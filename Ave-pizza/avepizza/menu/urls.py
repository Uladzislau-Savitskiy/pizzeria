from django.urls import path, re_path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.menu, name='menu'),
    path('pizza/', views.pizza, name='menu_pizza'),
    # path('pizza/<str:pizza>/', views.pizza),
    path('drinks/<str:drink>', views.drinks, name='menu_drinks'),
    path('archive/<year4:year>/', views.archive, name='archive'),
    # path('order_cart', views.add_order_cart, name='order_cart')

    ]
