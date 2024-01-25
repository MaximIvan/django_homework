import datetime
from django.core.management.base import BaseCommand
from homeworkapp_2.models import Client

class Command(BaseCommand):
    help = "Registration new client."

    def handle(self, *args, **kwargs):
        client = Client(
            name='Кристина',
            email='kris@example.com',
            phone='+79999999994',
            address='Мурманск, ул.Морская, 75, кв. 45',
            date_registered=datetime.date(2018, 12, 10)
            )
        client.save()
        self.stdout.write(self.style.SUCCESS(f'Клиент: {client} зарегистрирован.'))

    