""" 
View every single page extending basegeneric. The context_variables
should be inherited using Context Processors.

from django.template import RequestContext should be included on each
view that wishes to extend this page.

"""
from storefront.models.store.shop import Config

from django.views.generic.base import TemplateView


class BaseGeneric(TemplateView):
    
    template_name="storefront/base_generic.html"
	
    def get_context_data(self, **kwargs):
        context = super(FrontPage, self).get_context_data(**kwargs)
        context['company_info'] = Config.objects.all()
        return context
