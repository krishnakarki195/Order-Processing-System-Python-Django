from django.contrib import admin
from .models import Customer, Order

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','order',)

class OrderAdmin(admin.ModelAdmin):
    list_display= ('name',)

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order,OrderAdmin)