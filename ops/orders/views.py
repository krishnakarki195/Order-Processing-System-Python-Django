#from django.urls import reverse
from django.shortcuts import render
#from django.contrib.auth.models import User
from .models import Customer, MenuItem, Order
from .forms import CustomerForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse


def home(request):
    return render(request, 'orders/index.html',{})


def list_customer(request):
	customers = Customer.objects.all()
	return render(request,'orders/list_customer.html',{'customers': customers})

def create_customer(request):
	form = CustomerForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		#instance.user = request.user
		instance.save()
		# message success
		#messages.success(request, "Successfully Created")
		return HttpResponseRedirect(reverse('orders:list_customer'))
	context = {
		'form' : form,
	}
	return render(request, "orders/create_customer.html", context)

def update_customer(request):
	pass

def delete_customer(request):
	pass