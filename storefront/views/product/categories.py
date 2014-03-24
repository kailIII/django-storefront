from django.views.generic import ListView
from django.views.generic import DetailView
from storefront.models.product.categories import Category
from storefront.models.product.items import Item


class CategoryList(ListView):
    model = Category
    template_name = 'storefront/product/category_list.html'



class CategoryDetail(DetailView):
    model = Category
    template_name='storefront/product/category_detail.html'
 
