from .forms import OrderForm
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Customer, Order, MenuItem
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


# Home views
class Home(View):

    template_name= "index.html"

    def get(self, request,*args,**kwargs):
        return render(request,self.template_name,{})


# Customer related views
class CustomerList(View):
    pass


class CustomerDetail(View):
    pass


class CustomerCreate(View):
    pass


class CustomerUpdate(View):
    pass


class CustomerDelete(View):
    pass


# Menu related views
class MenuList(View):
    pass


class MenuDetail(View):
    pass


class MenuCreate(View):
    pass


class MenuUpdate(View):
    pass


class MenuDelete(View):
    pass


# Order related views
class OrderList(View):

    template_name= "list_order.html"

    def get(self, request,*args,**kwargs):
        context = {}
        orders = Order.objects.all()
        for order in Order.objects.all().prefetch_related('menuitems'):
            menuitems = list(order.menuitems.all())
            context[order.name]={'id':order.id,'name':order.name,'customer':order.customer,'menuitems':menuitems}

        return render(request,self.template_name,{'form':context})


class OrderDetail(View):

    template_name = "list_order.html"

    def get(self,request,id,*args,**kwargs):
        context = {}
        for order in Order.objects.filter(id=int(id)).prefetch_related('menuitems'):
            menuitems = list(order.menuitems.all())
            context[order.name]={'id':order.id,'name':order.name,'customer':order.customer,'menuitems':menuitems}

        return render(request,self.template_name,{'form':context})


class OrderCreate(View):

    template_name = "create_order.html"
    form_class = OrderForm

    def get(self, request,*args,**kwargs):
        form = self.form_class(initial={})
        return render(request,self.template_name,{'form':form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()
            messages.success(request,'create success!!')
            return HttpResponseRedirect(reverse('orders:list_order'))
        return render(request,self.template_name,{'form':form})


class OrderUpdate(View):

    template_name = "update_order.html"
    form_class = OrderForm

    def get(self,request,id,*args,**kwargs):
        ob = get_object_or_404(Order,id=id)
        form = self.form_class(instance=ob)
        return render(request,self.template_name,{'form':form})

    def post(self,request,id,*args,**kwargs):
        ob = get_object_or_404(Order,id=id)
        form = self.form_class(request.POST or None,instance=ob)
        if form.is_valid():
            instance = form.save(commit=False)
            instance
            instance.save()
            form.save_m2m()
            messages.success(request,'update success!!')
            return HttpResponseRedirect(reverse('orders:detail_order',kwargs={'id':instance.id}))
        return render(request,self.template_name,{'form':form})


class OrderDelete(View):

    def get(self, request,id,*args,**kwargs):
        ob = get_object_or_404(Order,id=id)
        ob.delete()
        return HttpResponseRedirect(reverse('orders:list_order'))