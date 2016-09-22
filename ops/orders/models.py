from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return(str(nickname))

class Order(models.Model):
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

    def __str(self):
        return (str(name))