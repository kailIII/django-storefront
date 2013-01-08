"""Defaults urls for the storefront project"""
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls import patterns
from django.views.generic.base import TemplateView

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name="storefront/storefront.html"), name="storefront_home"),
    url(r'^tags/', include('storefront.urls.tags')),
    url(r'^categories/', include('storefront.urls.product.categories')),
    url(r'^', include('storefront.urls.product.items')),
    )   
