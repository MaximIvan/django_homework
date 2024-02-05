from django.db import models

# Create your models here.

'''
Задание
Измените модель продукта, добавьте поле для хранения фотографии продукта.

Создайте форму, которая позволит сохранять фото.
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
    image_product = models.ImageField(upload_to="images/")

    def __str__(self):
        # return f'Название товара: {self.name_product}, Описание: {self.description}, цена: {self.price}, Количество: {self.quantity}'
        return self.name_product


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f' №Заказа: {self.id} от {self.date_ordered} клиент: {self.customer.name_client}'
    