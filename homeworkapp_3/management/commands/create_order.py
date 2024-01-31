import datetime
from django.core.management.base import BaseCommand
from homeworkapp_3.models import Client, Order, Product


class Command(BaseCommand):
    help = "Create order"

    def add_arguments(self, parser):
        parser.add_argument("id_client", type=int, help="client ID")
        parser.add_argument('-p', '--id_product', nargs='+', help="product ID", required=True)

    def handle(self, *args, **kwargs):
        id_client = kwargs.get('id_client')
        id_product: list = kwargs.get('id_product')               

        client = Client.objects.filter(pk=id_client).first()

        order = Order(customer=client)
            
        total_price = 0
        for i in range(0, len(id_product)):
            product = Product.objects.filter(pk=id_product[i]).first()
            total_price += float(product.price)
            order.total_price = total_price
            order.save()
            order.date_ordered=datetime.date()
            order.save()
            order.products.add(product)
            self.stdout.write(self.style.SUCCESS(f'Заказ: {order} создан.'))