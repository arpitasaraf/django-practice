from django.db import models

# Create your models here.

class Seller(models.Model):
    name = models.CharField(max_length=90)
    email = models.EmailField()
    gst_no = models.CharField(max_length=50)
    is_special_seller = models.BooleanField(default=False)

