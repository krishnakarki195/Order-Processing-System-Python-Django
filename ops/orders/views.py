from django.shortcuts import render
 

def home(request):
    return render(request, 'orders/base.html',{})