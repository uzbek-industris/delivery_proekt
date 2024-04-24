from django.db import models

class OrderInfo(models.Model):
    deliver_name = models.IntegerField()
    client = models.IntegerField()
    price = models.IntegerField()
    sity = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    home = models.IntegerField()
    entrance = models.IntegerField()
    floor = models.IntegerField()
    flat = models.IntegerField()
    comment = models.CharField(max_length=255)
    STATUS_CHOICES = [
        (0, 'В обработке'),
        (1, 'Принят'),
        (2, 'Готовится'),
        (3, 'Передан курьеру'),
        (4, 'Ждет курьера'),
        (5, 'Доставлен'),
        (6, 'Отказан'),
        (7, 'Отменен'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES)

class Users(models.Model):
    name = models.CharField(max_length=255)
    STATUS_CHOICES = [
        (0, 'Менеджер'),
        (1, 'Заказчик'),
        (2, 'Доставщик'),
        (3, 'Кухня'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES)

class Kitchen(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house = models.IntegerField()
    capacity = models.IntegerField()

    # def __str__(self):
    #     return self.name

