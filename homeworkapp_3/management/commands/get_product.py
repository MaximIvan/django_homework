from django.core.management.base import BaseCommand
from homeworkapp_3.models import Product


class Command(BaseCommand):
    help = "Get product by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        id_product = kwargs.get('pk')
        product = Product.objects.filter(pk=id_product).first()              
        self.stdout.write(f'{product}')