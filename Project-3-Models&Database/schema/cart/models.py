from django.db import models

# Create your models here.


class Cartitem(models.Model):
    name = models.CharField(max_length=100)
    seller_name = models.CharField(max_length=100)
    price = models.IntegerField()
    rating = models.IntegerField()
