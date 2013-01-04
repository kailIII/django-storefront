# Django settings for storefront project.

from django.conf import settings

PAGINATION = getattr(settings, 'STOREFRONT_PAGINATION', 10)
ITEM_TEMPLATES = getattr(settings, 'STOREFRONT_ITEM_TEMPLATES', [])
ITEM_BASE_MODEL = getattr(settings, 'STOREFRONT_ITEM_BASE_MODEL', '')
DEFAULT_CURRENCY = getattr(settings, 'STOREFRONT_DEFAULT_CURRENCY', '')
