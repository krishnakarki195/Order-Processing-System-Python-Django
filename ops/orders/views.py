from django.shortcuts import render
#from django.contrib.auth.models import User
from .models import Customer, MenuItem, Order
 

def home(request):
    return render(request, 'orders/index.html',{})


def list_customer(request):
	customers = Customer.objects.all()
	return render(request,'orders/list_customer.html',{'customers': customers})