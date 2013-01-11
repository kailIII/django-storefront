from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from storefront.models.product.items import Item
from storefront.models.product.items import ItemImage

from storefront.mixins import CompanyInfoMixin

class ItemDetail(DetailView, CompanyInfoMixin):
	
    model = Item
    slug_field = 'slug'
    template_name="storefront/product/item_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(ItemDetail, self).get_context_data(**kwargs)
        return context
