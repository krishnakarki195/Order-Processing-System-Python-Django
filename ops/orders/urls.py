
from django.conf.urls import url
from django.contrib import admin
from .views import (
        Home,
		# Order related views
        OrderList,
        OrderCreate,
        OrderDetail,
        OrderDelete,
        OrderUpdate,
        # Customer related views
        CustomerCreate,
        CustomerList,
        CustomerUpdate,
        CustomerDetail,
        CustomerDelete,
        # Menu related views
        MenuCreate,
        MenuList,
        MenuDetail,
        MenuUpdate,
        MenuDelete,
	)


urlpatterns = [
    url(r'^$',Home.as_view(), name='home'),
    # Order related urls
    url(r'^list_order/$',OrderList.as_view(), name='list_order'),
    url(r'^create_order/$',OrderCreate.as_view(),name='create_order'),
    url(r'^list_order/(?P<id>\d+)/$',OrderDetail.as_view(),name='detail_order'),
    url(r'^update_order/(?P<id>\d+)/$',OrderUpdate.as_view(),name='update_order'),
    url(r'^delete_order/(?P<id>\d+)/$',OrderDelete.as_view(),name='delete_order'),
    # Customer related urls
    url(r'^list_customer/$',CustomerList.as_view(), name='list_customer'),
    url(r'^create_customer/$',CustomerCreate.as_view(),name='create_customer'),
    url(r'^list_customer/(?P<id>\d+)/$',CustomerDetail.as_view(),name='detail_customer'),
    url(r'^update_customer/(?P<id>\d+)/$',CustomerUpdate.as_view(),name='update_customer'),
    url(r'^delete_customer/(?P<id>\d+)/$',CustomerDelete.as_view(),name='delete_customer'),
    # Menu related urls
    url(r'^list_menu/$',MenuList.as_view(), name='list_menu'),
    url(r'^create_menu/$',MenuCreate.as_view(),name='create_menu'),
    url(r'^list_menu/(?P<id>\d+)/$',MenuDetail.as_view(),name='detail_menu'),
    url(r'^update_menu/(?P<id>\d+)/$',MenuUpdate.as_view(),name='update_menu'),
    url(r'^delete_menu/(?P<id>\d+)/$',MenuDelete.as_view(),name='delete_menu'),
]

