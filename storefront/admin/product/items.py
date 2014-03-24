"""ItemAdmin for storefront"""
from django.contrib import admin
from storefront.models.product.items import Item
from storefront.models.product.items import ItemImage

class ItemImage_Inline(admin.StackedInline):
    model = ItemImage
    extra = 1

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",), 
    }
    search_fields = ['slug', 'sku', 'name']
    inlines = [ ItemImage_Inline ]


