from django.db import models

# Create your models here.

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    is_available = models.BooleanField(default=False)
    description = models.TextField()


class ProductOwner(models.Model):
    name = models.CharField(max_length=30)
    phoneNo = models.BigIntegerField()
    email = models.EmailField()

