from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=100)
    #customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    #url = models.UrlField(max_length=200)

    def __str(self):
        return (str(self.name))


class Customer(models.Model):
    name = models.CharField(max_length=100)
    #url = models.UrlField(max_length=200)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)

    def __str__(self):
        return(str(self.name))

