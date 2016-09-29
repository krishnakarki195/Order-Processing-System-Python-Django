from .forms import OrderForm, MenuItemForm, CustomerForm
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

    template_name= "list_customer.html"

    def get(self, request,*args,**kwargs):
        context = {}
        customers = Customer.objects.all()
        for customer in customers:
            context[customer.name] = {'id':customer.id,'name':customer.name}
        return render(request,self.template_name,{'customers':context})


class CustomerDetail(View):

    template_name = "detail_customer.html"

    def get(self,request,id,*args,**kwargs):
        customer = get_object_or_404(Customer,id=id)
        return render(request,self.template_name,{'customer':customer})


class CustomerCreate(View):

    template_name = "create_customer.html"
    form_class = CustomerForm

    def get(self, request,*args,**kwargs):
        form = self.form_class(initial={})
        return render(request,self.template_name,{'form':form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request,'Cusomer create successful !')
            return HttpResponseRedirect(reverse('orders:list_customer'))
        return render(request,self.template_name,{'form':form})


class CustomerUpdate(View):

    template_name = "update_customer.html"
    form_class = CustomerForm

    def get(self,request,id,*args,**kwargs):
        ob = get_object_or_404(Customer,id=id)
        form = self.form_class(instance=ob)
        return render(request,self.template_name,{'form':form})

    def post(self,request,id,*args,**kwargs):
        ob = get_object_or_404(Customer,id=id)
        form = self.form_class(request.POST or None,instance=ob)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request,'Customer update successful !')
            return HttpResponseRedirect(reverse('orders:detail_customer',kwargs={'id':instance.id}))
        return render(request,self.template_name,{'form':form})


class CustomerDelete(View):

    def get(self, request,id,*args,**kwargs):
        ob = get_object_or_404(Customer,id=id)
        ob.delete()
        return HttpResponseRedirect(reverse('orders:list_customer'))


# Menu related views
class MenuList(View):

    template_name= "list_menu.html"

    def get(self, request,*args,**kwargs):
        context = {}
        menus = MenuItem.objects.all()
        for menu in menus:
            context[menu.name] = {'id':menu.id,'name':menu.name}
        return render(request,self.template_name,{'menus':context})


class MenuDetail(View):

    template_name = "detail_menu.html"

    def get(self,request,id,*args,**kwargs):
        menu = get_object_or_404(MenuItem,id=id)
        return render(request,self.template_name,{'menu':menu})


class MenuCreate(View):

    template_name = "create_menu.html"
    form_class = MenuItemForm

    def get(self, request,*args,**kwargs):
        form = self.form_class(initial={})
        return render(request,self.template_name,{'form':form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request,'Menu create successful !')
            return HttpResponseRedirect(reverse('orders:list_menu'))
        return render(request,self.template_name,{'form':form})


class MenuUpdate(View):

    template_name = "update_menu.html"
    form_class = MenuItemForm

    def get(self,request,id,*args,**kwargs):
        ob = get_object_or_404(MenuItem,id=id)
        form = self.form_class(instance=ob)
        return render(request,self.template_name,{'form':form})

    def post(self,request,id,*args,**kwargs):
        ob = get_object_or_404(Order,id=id)
        form = self.form_class(request.POST or None,instance=ob)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request,'Menu update successful !')
            return HttpResponseRedirect(reverse('orders:detail_menu',kwargs={'id':instance.id}))
        return render(request,self.template_name,{'form':form})


class MenuDelete(View):

    def get(self, request,id,*args,**kwargs):
        ob = get_object_or_404(MenuItem,id=id)
        ob.delete()
        return HttpResponseRedirect(reverse('orders:list_menu'))


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

    template_name = "detail_order.html"

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