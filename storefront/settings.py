# Django settings for storefront project.

from django.conf import settings

PAGINATION = getattr(settings, 'STOREFRONT_PAGINATION', 10)
ITEM_TEMPLATES = getattr(settings, 'STOREFRONT_ITEM_TEMPLATES', [])
ITEM_BASE_MODEL = getattr(settings, 'STOREFRONT_ITEM_BASE_MODEL', '')
DEFAULT_CURRENCY = getattr(settings, 'STOREFRONT_DEFAULT_CURRENCY', '')
COMPANY_INFO = getattr(settings, 'STOREFRONT_COMPANY_INFO', {
			'name':'default name',
			'phone':'default phone',
			'fax':'default fax',
			'email':'default email',}
)

#For banner Add
BANNER_DISPLAY_TIMEOUT = getattr(settings, 'STOREFRONT_BANNER_DISPLAY_TIMEOUT', 2000)
