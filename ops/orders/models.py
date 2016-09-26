from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from decimal import Decimal


class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return(str(self.name))

class Order(models.Model):
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.name))

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    order = models.ManyToManyField(Order,blank=True,related_name='menuitems')

    def __str__(self):
        return (str(self.name))

#url = models.UrlField(max_length=200)
# =======
# # Create your models here.
# class Customer(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
#     phone = PhoneNumberField()
#     dob = models.DateField()
#     street = models.CharField(max_length=120)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=80)
#     zip_code = models.IntegerField()
#     country = models.CharField(max_length=120)
# >>>>>>> Stashed changes
# =======
#     status = models.CharField(max_length=20)

#     def __str__(self):
#         return (str(self.name))
# >>>>>>> Stashed changes

# class MenuItem(models.Model):
#     name = models.CharField(max_length=200)
#     ingredients = models.CharField(max_length=200)
#     price = models.DecimalField(max_digits=20,decimal_places=2,default=Decimal('0.00'))
#     order = models.ForeignKey(Order,on_delete=models.CASCADE)
#     def __str__(self):
#         return (str(self.name))