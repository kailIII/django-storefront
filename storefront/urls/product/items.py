"""Urls for the storefront items"""
from django.conf.urls import url
from django.conf.urls import patterns

from storefront.views.product.items import ItemDetail

urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[-\w]+)/$',
	        ItemDetail.as_view(),
	        name="storefront_item_detail"),
)
