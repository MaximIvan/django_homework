from django.core.management.base import BaseCommand
from homeworkapp_3.models import Product


class Command(BaseCommand):
    help = "update product price by id product"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='id of products')
        parser.add_argument('price', type=float, help="price of product")

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        price = kwargs.get('price')
        product = Product.objects.filter(pk=pk).first()          
        product.price = price
        product.save()                                                 
        self.stdout.write(f'{product}')