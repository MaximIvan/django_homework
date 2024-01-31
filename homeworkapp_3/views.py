from django.shortcuts import render
from django.http import HttpResponse
from homeworkapp_3.models import Client, Order, Product
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

def index(request):
    return render(request, 'homeworkapp_3/index.html')


# вывод всех товаров
def products(request):
    products = Product.objects.all()
    return render(request, 'homeworkapp_3/products.html', {'products': products})


# вывод списка всех клиентов
def clients(request):
    clients = Client.objects.all()
    return render(request, 'homeworkapp_3/clients.html', {'clients': clients})


# вывод заказа по  id
def order(request, id_order: int):
    order = Order.objects.get(pk=id_order)
    context = {
        'order': order
    }
    return render(request, 'homeworkapp_3/order.html', context=context)


# вывод списка заказов
def orders(request):
    products_all = []
    orders = Order.objects.all()

    context = {
        'orders': orders
    }
    return render(request, 'homeworkapp_3/orders_all.html', context=context)


def client_orders(request, id_client: int):
    products = {}

    client = Client.objects.filter(pk=id_client).first()
    orders = Order.objects.filter(customer=client).all()

    for order in orders:
        products[order.id] = str(order.products.all()).replace('<QuerySet [<', '').replace('>]>', '').split('>, <')

    return render(request, 'homeworkapp_3/client_orders.html', {'client': client, 'orders': orders, 'products': products})


def product(request, id_product: int):
    product = Product.objects.filter(pk=id_product).first()
    context = {
        "product": product

    }
    return render(request, "homeworkapp_3/product.html", context=context)


def client_products_sorted(request, id_client: int, days: int):
    products = []
    product_set = []
    now = datetime.now()
    before = now - timedelta(days=days)
    client = Client.objects.filter(pk=id_client).first()
    orders = Order.objects.filter(customer=client, date_create_order__range=(before, now)).all()
    for order in orders:
        products = order.products.all()
        for product in products:
            if product not in product_set:
                product_set.append(product)

    return render(request, 'homeworkapp_3/client_all_products_from_orders.html',
                  {'client': client, 'product_set': product_set, 'days': days})

