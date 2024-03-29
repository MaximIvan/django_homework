from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),                                            #вывод главной страницы
    path('shop/products/', views.products, name='products'),                        #вывод списка всей продукции
    path('shop/clients/', views.clients, name='clients'),                           # вывод всех клиентов
    path('shop/orders/', views.orders, name='orders'),                              # вывод всех заказов
    path('shop/client_products_sorted/<int:id_client>/<int:days>/', views.client_products_sorted, name='client_products_sorted'), # вывыод всех товаров по клиенту за последние кол дней
]