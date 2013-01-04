from django.conf.urls.defaults import *

from storefront.views.product.categories import CategoryList
#from storefront.views.product.categories import CategoryDetail

urlpatterns = patterns(
    '',
    url(r'^$', CategoryList.as_view(), name='storefront_category_list'),
    #url(r'^(?P<parent_slugs>[-\/\w]+)/page/(?P<page>\d+)/$',    CategoryDetail.as_view(), name='storefront_category_detail_paginated'),
    #url(r'^(?P<parent_slugs>([-\w]+/)*)?(?P<slug>[-\w]+)/$', CategoryDetailed.as_view(), name='storefront_category_details'),
)
