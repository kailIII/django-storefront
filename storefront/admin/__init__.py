"""Admin of storefront"""
from django.contrib import admin

from storefront.models.product.items import Item
from storefront.admin.product.items import ItemAdmin

from storefront.models.product.categories import Category
from storefront.admin.product.categories import CategoryAdmin

from storefront.models.l10n.country import Country
from storefront.admin.l10n.country import CountryAdmin

from storefront.models.store.shop import Config
from storefront.admin.store.shop import ConfigAdmin

from storefront.models.frontend.banners import Banner
from storefront.admin.frontend.banners import BannerAdmin


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Config, ConfigAdmin)
admin.site.register(Banner, BannerAdmin)
