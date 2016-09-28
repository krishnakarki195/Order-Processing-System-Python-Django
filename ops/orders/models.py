from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.CharField(max_length=100)
    #url = models.UrlField(max_length=200)

    def __str__(self):
        return(str(self.name))

class MenuItem(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return (str(self.name))


class Order(models.Model):
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    menuitems = models.ManyToManyField(MenuItem,blank=True,related_name='orders')

    def __str__(self):
        return (str(self.name))










