"""CategoryAdmin for storefront"""
from django.contrib import admin
from storefront.models.product.items import Item
from storefront.models.product.categories import Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
