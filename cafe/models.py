from django.db import models

# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    server = models.BooleanField(verbose_name="Обслуживает клиентов", default=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

class Employee(models.Model):
    fullname = models.CharField(max_length=255, verbose_name="ФИО")
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Должность")
    
    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'    


class Provider(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
    

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    count = models.IntegerField(verbose_name="Количество")
    provider = models.ManyToManyField(Provider, verbose_name="Поставщик")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Menu(models.Model):
    dish_name = models.CharField(max_length=255, verbose_name="Название блюда")
    price = models.IntegerField(verbose_name="Цена")
    products = models.ManyToManyField(Product, verbose_name="Продукты")

    def __str__(self):
        return self.dish_name
    
    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    

class Order(models.Model):
    client_name = models.CharField(max_length=255, verbose_name="Имя клиента")
    created_time = models.DateTimeField(verbose_name="Дата создания", auto_now=True)
    dishes = models.ManyToManyField(Menu, verbose_name="Блюда")
    served_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Обслуживающий сотрудник")
    total_price = models.IntegerField(verbose_name="Итоговая цена")

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"