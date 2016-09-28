# from django import forms
# from .models import MenuItem, Customer

# class OrderForm(forms.ModelForm):
#     menuitems = forms.ModelMultipleChoiceField(
#         MenuItem.objects.all(),
#         required=True
#         )
#     def __init__(self,*args,**kwargs):
#         super(OrderForm,self).__init__(*args,**kwargs)
#         if self.instance.pk:
#             self.initial['menuitems']= self.instance.menuitems.values_list('pk',flat=True)

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

# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = [
#             "name",
#         ]