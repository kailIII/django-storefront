"""ConfigAdmin for storefront"""
from django.contrib import admin

from storefront.models.store.shop import Config
    
class ConfigAdmin(admin.ModelAdmin):
    pass
    
