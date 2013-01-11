from django.views.generic.detail import SingleObjectMixin

from storefront.settings import COMPANY_INFO

class CompanyInfoMixin(SingleObjectMixin):
    	
    def get_context_data(self, **kwargs):
        context = super(CompanyInfoMixin, self).get_context_data(**kwargs)
        context['company_name'] = COMPANY_INFO['NAME']
        context['company_phone'] = COMPANY_INFO['PHONE']
        context['company_fax'] = COMPANY_INFO['FAX']
        context['company_email'] = COMPANY_INFO['EMAIL']
        return context
