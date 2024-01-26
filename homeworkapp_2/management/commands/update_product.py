from django.core.management.base import BaseCommand
from homeworkapp_2.models import Product


class Command(BaseCommand):
    help = "Update product price and quantity by id."
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='product ID')
        parser.add_argument('price', type=float, help='product price')
        parser.add_argument('quantity', type=int, help='product quantity')
    
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        price = kwargs.get('price')
        quantity = kwargs.get('quantity')
        product = Product.objects.filter(pk=pk).first()
        product.price = price
        product.quantity = quantity
        product.save()
        self.stdout.write(f'{product}')