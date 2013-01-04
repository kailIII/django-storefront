"""Urls for the storefront tags"""
from django.conf.urls import url
from django.conf.urls import patterns

from storefront.views.tags import TagList
from storefront.views.tags import TagDetail


urlpatterns = patterns(
    '',
    url(r'^$',  TagList.as_view(),  name='storefront_tag_list'),
    url(r'^(?P<tag>[^/]+(?u))/$', TagDetail.as_view(), name='storefront_tag_detail'),
    url(r'^(?P<tag>[^/]+(?u))/page/(?P<page>\d+)/$', TagDetail.as_view(), name='storefront_tag_detail_paginated'),
    )
