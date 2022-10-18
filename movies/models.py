from django.db import models


class Users(models.Model):
    fio = models.CharField(max_length=255, verbose_name="ФИО")
    email = models.CharField(max_length=50, verbose_name="E-mail")
    phone = models.PositiveBigIntegerField(verbose_name="Номер телефона")


class Films(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.CharField(max_length=255, verbose_name="Описание")
    genres = models.CharField(max_length=255, verbose_name="Жанры")
    country = models.CharField(max_length=255, verbose_name="Страна")
    year = models.IntegerField(verbose_name="Год")


class Seats(models.Model):
    number = models.IntegerField(verbose_name="Номер места")
    row = models.IntegerField(verbose_name="Ряд")
    hall = models.IntegerField(verbose_name="Зал")
    price = models.FloatField(verbose_name="Стоимость")


class Orders(models.Model):
    STATUS = (
        ('R', 'Registered'),
        ('W', 'In work'),
        ('C', 'Completed'),
        ('D', 'Deleted'),
    )
    order_data = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")
    film_data = models.DateField(auto_now=True, verbose_name="Дата сеанса")
    film_time = models.TimeField(auto_now=True, verbose_name="Время сеанса")
    status = models.CharField(max_length=1, choices=STATUS, verbose_name="Сатус")
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    film = models.ForeignKey(Films, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seats, on_delete=models.CASCADE)

