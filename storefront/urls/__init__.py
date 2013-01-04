"""Defaults urls for the storefront project"""
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls import patterns

urlpatterns = patterns(
    '',
    url(r'^tags/', include('storefront.urls.tags',)),
    url(r'^categories/', include('storefront.urls.product.categories')),
    url(r'^', include('storefront.urls.product.items')),
    )
