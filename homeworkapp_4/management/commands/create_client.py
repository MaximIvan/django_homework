import datetime
from django.core.management.base import BaseCommand
from homeworkapp_4.models import Client

class Command(BaseCommand):
    help = "Registration new client."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='client name')
        parser.add_argument('email', type=str, help='client email')
        parser.add_argument('phone', type=str, help='client phone')
        parser.add_argument('address', type=str, help='client address')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        address = kwargs.get('address')
        date_registered=datetime.date(2018, 12, 10)
        
        client = Client(
            name_client=name,
            email=email,
            phone=phone,
            address=address,
            date_registered=date_registered
        )
        client.save()
        self.stdout.write(self.style.SUCCESS(f'Клиент: {client} зарегистрирован.'))