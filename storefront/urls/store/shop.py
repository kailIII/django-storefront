from django.conf.urls import url
from django.conf.urls import patterns

from django.views.generic.base import TemplateView

from storefront.views.store.shop import FrontPage


urlpatterns = patterns(
    '',
    
    url(r'^$',
			FrontPage.as_view(),
			name="storefront_home"),
			
	url(r'^about/$',
			TemplateView.as_view(template_name="storefront/about.html"),
			name="storefront_about"),
			
	url(r'^contact/$',
			TemplateView.as_view(template_name="storefront/contact.html"),
			name="storefront_contact"),
			
	url(r'^blog/$',
			TemplateView.as_view(template_name="storefront/blog.html"),
			name="storefront_blog"),
)


    
    
