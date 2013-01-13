"""
A set of request processors that return dictionaries to be merged into a
template context. Each function takes the request object as its only parameter
and returns a dictionary to add to the context.

These are referenced from the setting TEMPLATE_CONTEXT_PROCESSORS and used by
RequestContext.
"""

from storefront.settings import COMPANY_INFO
from django.middleware.csrf import get_token
from django.utils.functional import lazy

def settings(request):
    """
    Adds settings-related context variables to the context.
    """
    return {
        'COMPANY_NAME': COMPANY_INFO['name'],
        'COMPANY_PHONE': COMPANY_INFO['phone'],
        'COMPANY_FAX': COMPANY_INFO['fax'],
        'COMPANY_EMAIL': COMPANY_INFO['email'],
    }
