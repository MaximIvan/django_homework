from django.db import models

# Create your models here.

'''
Задание №7
Доработаем задачу 8 из прошлого семинара про клиентов,
товары и заказы.
Создайте шаблон для вывода всех заказов клиента и
списком товаров внутри каждого заказа.
Подготовьте необходимый маршрут и представление.

Создайте шаблон, который выводит список заказанных
клиентом товаров из всех его заказов с сортировкой по
времени:
○ за последние 7 дней (неделю)
○ за последние 30 дней (месяц)
○ за последние 365 дней (год)
*Товары в списке не должны повторятся.
'''

class Client(models.Model):
    name_client = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.TextField()
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return f'Имя клиента: {self.name_client}, Эл.почта:{self.email}, Телефон:{self.phone}'
        return self.name_client
    
class Product(models.Model):
    name_product = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return f'Название товара: {self.name_product}, Описание: {self.description}, цена: {self.price}, Количество: {self.quantity}'
        return self.name_product


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' №Заказа: {self.id} от {self.date_ordered} клиент: {self.customer.name_client}'
    