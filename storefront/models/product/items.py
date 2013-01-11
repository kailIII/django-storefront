import warnings

from django.db import models
from django.utils import timezone
from django.contrib import comments

from django.contrib.comments.models import CommentFlag
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel
from mptt.models import TreeForeignKey
from mptt.managers import TreeManager

from storefront.models.product.categories import Category
from storefront.managers import items_published
from storefront.managers import ItemPublishedManager
from storefront.managers import SALE, REGULAR

from storefront.settings import ITEM_BASE_MODEL
 
class ItemAbstractClass(models.Model):
    """ Base Model design for all items """
    
    STATUS_CHOICES = ((SALE, _('sale')), (REGULAR, _('regular')))
    
    name = models.CharField(_("Full Name"), max_length=255, blank=False,)
    slug = models.SlugField(_("Slug Name"), blank=True, unique=True, help_text=_("Used for URLs, auto-generated from name if blank"), max_length=255)
    sku = models.CharField(_("SKU"), max_length=255, blank=True, null=True,  help_text=_("Defaults to slug if left blank"))
    short_description = models.TextField(_("Short description of the item"), max_length=200, default='', blank=True)
    description = models.TextField(_("Description of the item"),  default='', blank=True)
    categories = models.ManyToManyField(Category, verbose_name=_("Category"), related_name='items', blank=True, null=True)
    items_in_stock = models.IntegerField(_("Number in stock"), default='0')
    meta_description = models.TextField(_("Meta Description"), max_length=200, blank=True, null=True, help_text=_("Meta description for this item"))
    ordering = models.IntegerField(_("Ordering"), default=0, help_text=_("Override alphabetical order in category display"))
    featured = models.BooleanField(_('Featured'), default=False)
    is_active = models.BooleanField(_("Active"), default=True, blank=True)
    comment_enabled = models.BooleanField(_('comment enabled'), default=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=REGULAR)
    creation_date = models.DateTimeField(_('creation date'), default=timezone.now)
    start_sale = models.DateTimeField(_('start sale'), blank=True, null=True, help_text=_('date start sale'))
    end_sale = models.DateTimeField(_('end sale'), blank=True, null=True, help_text=_('date end sale'))

    def __unicode__(self):
        return self.name
        
    @models.permalink
    def get_absolute_url(self):
        """Return entry's URL"""
        return ('storefront_item_detail', (), {
            'slug': self.slug})

    class Meta:
        """ Item's Meta """
        abstract = True
        app_label = 'storefront'
        ordering = ('ordering', 'name')
        verbose_name = _("Item")
        verbose_name_plural = _("Items")

class Item(ItemAbstractClass):
    """
    The final model based on inheritance
    """
    
class ItemImage(models.Model):
    """
    A picture of an item.  Can have many pictures associated per item.
    """
    item = models.ForeignKey(Item, null=True, blank=True)
    picture = models.ImageField(upload_to="images/", blank=True, null=True)
    caption = models.CharField(_("Optional caption"), max_length=100, null=True, blank=True)
    sort = models.IntegerField(_("Sort Order"), default=0)
    
    def __unicode__(self):
        if self.caption:
            return u"%s" % self.caption
        else:
            return u"%s" % self.picture

    class Meta:
        app_label = 'storefront'
        ordering = ['sort']
        verbose_name = _("Item Image")
        verbose_name_plural = _("Item Images")

 



