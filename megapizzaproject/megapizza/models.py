from django.db import models
from django.contrib.auth.models import User

class Tovar(models.Model):
    brand = models.CharField(max_length=100)
    fullname = models.CharField(max_length=400)
    image = models.ImageField(upload_to='megapizza/static/images')
    description = models.TextField()
    price = models.FloatField()
    def __str__(self):
        return str(self.id) + ' ' + str(self.fullname)
    
class Corf(models.Model):
    tovar = models.ForeignKey(Tovar, on_delete=models.PROTECT, null=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)

    
class OrderInfo(models.Model):
    STATUS = (
        ('0', 'Принят'),
        ('1', 'На кухне'),
        ('2', 'У курьера'),
        ('3', 'Доставлен'),
        ('4', 'Отменён'),
        ('5', 'Не обработан'),
    )
    id = models.AutoField(primary_key=True)
    deliver_name = models.TextField()
    client = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    price = models.IntegerField()
    sity = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    home = models.IntegerField()
    entrance = models.IntegerField()
    floor = models.IntegerField()
    flat = models.IntegerField()
    comment = models.TextField()
    status = models.CharField(max_length=3, choices=STATUS)

class Kitchen(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.city

