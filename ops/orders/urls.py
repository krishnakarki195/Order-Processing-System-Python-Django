
from django.conf.urls import url
from django.contrib import admin
from .views import (
		OrderList,
        OrderCreate,
        OrderDetail,
        OrderDelete,
        OrderUpdate
	)


urlpatterns = [
    url(r'^$',OrderList.as_view(), name='list'),
    url(r'^create/$',OrderCreate.as_view(),name='create'),
    url(r'^(?P<id>\d+)/$',OrderDetail.as_view(),name='detail'),
    url(r'^(?P<id>\d+)/update/$',OrderUpdate.as_view(),name='update'),
    url(r'^(?P<id>\d+)/delete/$',OrderDelete.as_view(),name='delete'),

]

