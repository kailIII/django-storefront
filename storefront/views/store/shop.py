""" view for storefront frontpage"""

from storefront.models.product.categories import Category
from storefront.models.product.items import Item
from storefront.models.store.shop import Config

from django.views.generic.base import TemplateView


class FrontPage(TemplateView):
    """
    Most generic view type to start with.
    We'll customize with mixins.
    """
    
    template_name="storefront/storefront.html"
	
    def get_context_data(self, **kwargs):
        context = super(FrontPage, self).get_context_data(**kwargs)
        context['feature_list'] = Item.objects.filter(featured=True)
        context['category_list'] = Category.objects.all()
        context['company_info'] = Config.objects.all()
        return context

