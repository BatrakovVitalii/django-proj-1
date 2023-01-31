from django.db import models

# Create your models here.


class Coffee(models.Model):
    name = models.CharField(max_length=64)
    V = models.IntegerField(blank=False)
    price = models.IntegerField(blank=False)
    coffee_list = models.ManyToManyField('Topping')

class Topping(models.Model):
    title_topping = models.CharField(max_length=32)
    price = models.IntegerField(blank=True, default=0)

class Orders(models.Model):
    chat_id = models.IntegerField()
    client_name = models.CharField(max_length=24)
    total_coasts = models.FloatField(null=True)
    order_list = models.ManyToManyField('Coffee')
