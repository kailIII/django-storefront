"""ProducstsAdmin for storefront"""
from django.contrib import admin
from storefront.models.product.items import Item
from storefront.models.product.items import ItemImage
from storefront.models.product.categories import Category

class ItemImage_Inline(admin.StackedInline):
    model = ItemImage
    extra = 3

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",), 
        "sku": ("name",),
    }
    
    fieldsets = (
        (None, {'fields': ('site', 'categories', 'name', 'slug', 'sku', 'description', 'short_description', 'is_active', 'featured', 'items_in_stock','ordering', )}),
        #(_('Meta Data'), {'fields': ('meta',), 'classes': ('collapse',)}),
        #(_('Item Dimensions'), {'fields': (('length', 'length_units','width','width_units','height','height_units'),('weight','weight_units')), 'classes': ('collapse',)}),
        #(_('Tax'), {'fields':('taxable', 'taxClass'), 'classes': ('collapse',)}),
        #(_('Related Products'), {'fields':('related_items','also_purchased'),'classes':('collapse',)}), 
    )

    search_fields = ['slug', 'sku', 'name']
    inlines = [ ItemImage_Inline ]


