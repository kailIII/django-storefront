from django.conf.urls import url
from django.conf.urls import patterns

from storefront.views.product.categories import CategoryList
from storefront.views.product.categories import CategoryDetail


urlpatterns = patterns(
    '',
    
    url(r'^$',
			CategoryList.as_view(),
			name='storefront_category_list'),
	
    url(r'^(?P<parent_slugs>([-\w]+/)*)?(?P<slug>[-\w]+)/$',
			CategoryDetail.as_view(),
			name='storefront_category_detail'),
)
