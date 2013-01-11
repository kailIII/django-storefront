from django.conf.urls import url
from django.conf.urls import patterns

from storefront.views.common import HomePage
from storefront.views.common import AboutPage
from storefront.views.common import ContactPage

urlpatterns = patterns(
    '',  
    url(r'^$', HomePage.as_view(), name="storefront_home"),	
	url(r'^about/$', AboutPage.as_view(), name="storefront_about"),
	url(r'^contact/$', ContactPage.as_view(), name="storefront_contact"),
)


    
    
