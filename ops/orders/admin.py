from django.contrib import admin
from .models import Customer, Order, MenuItem
from .forms import OrderForm


class CustomerAdmin(admin.ModelAdmin):
    fields = ('name',)

class OrderAdmin(admin.ModelAdmin):
    fields= ('name','customer','menuitems',)

class MenuItemAdmin(admin.ModelAdmin):
    fields = ('name',)


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(MenuItem,MenuItemAdmin)

# =======
# # Register your models here.
# class CustomerAdmin(admin.ModelAdmin):
# 	"""docstring for CustomerAdmin"""
# 	list_display = ['name','phone','email']
# 	list_filter = []
# 	list_display_links = ['name']
# 	search_fields = ['name','email','phone']
# 	list_editable = []

# 	class meta:
# 		"""docstring for meta"""
# 		model = Customer


# class OrderAdmin(admin.ModelAdmin):
# 	"""docstring for OrderAdmin"""
# 	list_display= ['name','customer']
# 	list_filter = []
# 	list_display_links = ['name']
# 	search_fields = ['name','customer']
# 	list_editable = []

# 	class meta:
# 		"""docstring for meta"""
# 		model = Order


# class MenuItemAdmin(admin.ModelAdmin):
# 	"""docstring for MenuItemAdmin"""
# 	list_display = ['name','ingredients','price']
# 	list_filter = []
# 	list_display_links = ['name']
# 	search_fields = ['name','ingredients']
# 	list_editable = ['ingredients']

# 	class meta:
# 		"""docstring for meta"""
# 		model = MenuItem
# >>>>>>> Stashed changes