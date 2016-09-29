from django import forms
from .models import MenuItem, Order
from django.db.models.fields.related import ManyToManyRel
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from .models import MenuItem
from django.contrib import admin
from .models import Customer,MenuItem,Order


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields=['name','customer','menuitems']


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name']

# class _OrderForm(forms.ModelForm):
#     menuitems = forms.ModelMultipleChoiceField(
#         MenuItem.objects.all(),
#         required=True
#         )
#     def __init__(self,*args,**kwargs):
#         super(OrderForm,self).__init__(*args,**kwargs)
#         if self.instance.pk:
#             self.initial['menuitems']= self.instance.menuitems.values_list('pk',flat=True)
#         #rel = ManyToManyRel(to=MenuItem,through=Order)
#         #self.fields['menuitems'].widget = RelatedFieldWidgetWrapper(self.fields['menuitems'].widget,rel,admin.site)


#     def save (self,*args,**kwargs):
#         instance = super(OrderForm,self).save(*args,**kwargs)

#         if instance.pk:
#             for item in instance.menuitems.all():
#                 if item not in self.cleaned_data['menuitems']:
#                     instance.menuitems.remove(item)
#             for item in self.cleaned_data['menuitems']:
#                 if item not in instance.menuitems.all():
#                     instance.menuitems.add(item)
#         return instance
#     class Meta:
#         model = Order
#         fields = ['name','customer']