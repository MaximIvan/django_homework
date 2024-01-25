from django.db import models

# Create your models here.

'''
Задание
Создайте три модели Django: клиент, товар и заказ.

Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.

Поля модели «Клиент»:
— имя клиента
— электронная почта клиента
— номер телефона клиента
— адрес клиента
— дата регистрации клиента

Поля модели «Товар»:
— название товара
— описание товара
— цена товара
— количество товара
— дата добавления товара

Поля модели «Заказ»:
— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
— связь с моделью «Товар», указывает на товары, входящие в заказ
— общая сумма заказа
— дата оформления заказа

Допишите несколько функций CRUD для работы с моделями по желанию.
'''

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.TextField()
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Имя клиента: {self.name}, Эл.почта:{self.email}, Телефон:{self.phone}'
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Название товара: {self.title}, Описание: {self.description}, цена: {self.price}, Количество: {self.quantity}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

