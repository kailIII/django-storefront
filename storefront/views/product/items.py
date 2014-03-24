from django.views.generic import DetailView
from storefront.models.product.items import Item

class ItemDetail(DetailView):
    model = Item
    template_name="storefront/product/item_detail.html"
