"""Views for storefront categories"""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.shortcuts import get_object_or_404

from storefront.models.product.categories import Category
from storefront.models.product.items import Item


class CategoryList( ListView ):
    """
    View returning a list of all the categories, and
    their respective sub-categories
    """
    model = Category
    queryset = Category.objects.all()
    context_object_name='complete_category_list',
    template_name='storefront/product/category_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        return context


class CategoryDetail( DetailView ):
    """
    This view will give the category name and description and list off:
    - The name of each subcategory.
    - The name of each item in this category.
    - A description of that item.
    """

    model = Category
    slug_field = 'slug'
    template_name='storefront/product/category_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        return context
 
