from django.db import models

# Create your models here.


class Coffee(models.Model):

    name = models.CharField(max_length=64)
    V = models.IntegerField(blank=False)
    price = models.IntegerField(blank=False)

