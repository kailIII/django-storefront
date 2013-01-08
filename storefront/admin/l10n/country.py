"""CountryAdmin for storefront"""
from django.contrib import admin
from storefront.models.l10n.country import Country
from storefront.models.l10n.country import AdminArea


class ItemImage_Inline(admin.StackedInline):
    model = AdminArea
    extra = 1
    
    
class CountryAdmin(admin.ModelAdmin):
    inlines = [ ItemImage_Inline ]
    
