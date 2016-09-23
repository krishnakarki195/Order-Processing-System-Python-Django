from django.conf.urls import url
from django.contrib import admin
from .views import (
		home,
		list_customer,
	)

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^customer/', list_customer, name='list_customer'),
]