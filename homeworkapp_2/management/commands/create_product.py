import datetime
from django.core.management.base import BaseCommand
from homeworkapp_2.models import Product

class Command(BaseCommand):
    help = "Create new product."

    def handle(self, *args, **kwargs):
        product = Product(
            title='Конструктор',
            description='Lorem ipsum',
            price=5_640.25,
            quantity=63,
            date_added=datetime.date(2018, 12, 10)
            )
        product.save()
        self.stdout.write(self.style.SUCCESS(f'Товар: {product} добавлен.'))