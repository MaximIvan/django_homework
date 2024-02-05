import datetime
from django.core.management.base import BaseCommand
from homeworkapp_3.models import Product

class Command(BaseCommand):
    help = "Create new product."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='name of product')
        parser.add_argument('description', type=str, help='description of product')
        parser.add_argument('price', type=float, help='price of product')
        parser.add_argument('quantity', type=int, help='quantity of product')
        parser.add_argument('date_added', type=str, help='date of product')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        quantity = kwargs.get('quantity')
        date_added=datetime.date()

        product = Product(
            name_product=name,
            description=description,
            price=price,
            quantity=quantity,
            date_added=date_added
        )
        product.save()
        self.stdout.write(self.style.SUCCESS(f'Товар: {product} добавлен.'))