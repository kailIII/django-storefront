"""
Managers for storefront
The purpose of a manager is to make model querries.
Field queries should be implemented as functions in the model class itself.
If you find multiple classes require the same field querry, an abstract class may be in order.

Manager methods is the preferred way to add "table-level" functionality to your models. 
(For "row-level" functionality 
-- i.e., functions that act on a single instance of a model object 
-- use Model methods, not custom Manager methods.)

CURRENTLY NOT USED!
"""

from django.db import models
from django.db.models import Q
from django.contrib.sites.models import Site

REGULAR = 0
SALE= 1

def tags_published():
    """Return the published tags"""
    from tagging.models import Tag
    from storefront.models.product.items import Item
    tags_entry_published = Tag.objects.usage_for_queryset(Item.published.all())
    # Need to do that until the issue #44 of django-tagging is fixed
    return Tag.objects.filter(name__in=[t.name for t in tags_entry_published])

def items_published(queryset):
    """ Return only the active products with positive stock """
    return queryset.filter( 
        #models.Q( items_in_stock > 0 ),
        models.Q( is_active=True ),
    )

class ItemPublishedManager(models.Manager):
    """Manager to retrieve published entries"""

    def get_query_set(self):
        """Return published entries"""
        return items_published(
            super(ItemPublishedManager, self).get_query_set())
            
    def get_images(self):
        """Return related images"""
        from storefront.models.product.items import ItemImage
        return ItemImage.objects.filter(pk=ItemImage_id)


    def basic_search(self, pattern):
        """Basic search on entries"""
        lookup = None
        for pattern in pattern.split():
            query_part = models.Q(content__icontains=pattern) | \
                         models.Q(excerpt__icontains=pattern) | \
                         models.Q(name__icontains=pattern)
            if lookup is None:
                lookup = query_part
            else:
                lookup |= query_part

        return self.get_query_set().filter(lookup)

