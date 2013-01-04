"""Admin of storefront"""
from django.contrib import admin

from storefront.models.product.items import Item
from storefront.models.product.categories import Category
from storefront.admin.product.items import ItemAdmin
from storefront.admin.product.categories import CategoryAdmin


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
