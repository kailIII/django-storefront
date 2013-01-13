from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.shortcuts import get_object_or_404

from storefront.models.product.categories import Category
from storefront.models.product.items import Item

from storefront.settings import COMPANY_INFO

class CategoryList( ListView ):

    model = Category
    queryset = Category.objects.all()
    context_object_name='complete_category_list',
    template_name='storefront/product/category_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        return context


class CategoryDetail( DetailView ):

    model = Category
    slug_field = 'slug'
    template_name='storefront/product/category_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        return context
 
