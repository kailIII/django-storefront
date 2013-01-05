""" Views for storefront entries """
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.list import BaseListView

from django.shortcuts import get_object_or_404

from storefront.models.product.items import Item
from storefront.models.product.categories import Category

class ItemDetail(TemplateView):
    """
    Shows all the details of an item, such as:
    - number in stock
    - price
    - description
    - images
    """
    
    template_name="product/item_detail.html"
    
    #item = get_object_or_404(Item, slug__iexact=self.kwargs['slug'])
    #products = list(self.item.__collumn__(),) #replace __ with a name,
    
    def get_queryset(self):
        category = get_object_or_404(Category, slug__iexact=self.kwargs['slug'])
        return Category.objects.get_by_site(slug=slug)
    
    def get_context_data(self, **kwargs):
        context = super(ItemDetail, self).get_context_data(**kwargs)
        context['item'] =  get_object_or_404(Item, slug__iexact=self.kwargs['slug'])
        context['name'] = self.item.name
        context['description'] = self.item.description
        #context['sale'] = find_best_auto_discount(self.products)
        #contect['child_categories'] = category.get_all_children()
        return context

