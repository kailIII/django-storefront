"""BannerAdmin for storefront"""
from django.contrib import admin
from storefront.models.frontend.banners import Banner

class BannerAdmin(admin.ModelAdmin):
    pass
