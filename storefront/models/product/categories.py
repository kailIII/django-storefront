"""Category model for storefront"""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel
from mptt.models import TreeForeignKey
from mptt.managers import TreeManager

from sorl.thumbnail import ImageField

from storefront.managers import items_published

class Category(MPTTModel):
    """Category model for Item"""

    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(help_text=_('Used to generate URL. If left blank, this will be generated from the name field.'), unique=True, max_length=255)
    description = models.TextField(_('description'), blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, verbose_name=_('parent category'), related_name='children')
    meta_description = models.TextField(_("Meta Description"), max_length=200, blank=True, null=True,  help_text=_("Meta description for this category"))
    ordering = models.IntegerField(_("Ordering"), default=0, help_text=_("Override alphabetical order in category display"))
    is_active = models.BooleanField(_("Active"), default=True, blank=True)
    related = models.ManyToManyField('self', verbose_name=_('related categories'), blank=True, null=True)
    image = models.ImageField("Category Image", upload_to="images/", blank=True, null=True)

    objects = TreeManager()

    
    def __unicode__(self):
        return self.name

    def items_published(self):
        """Return only the entries published"""
        return items_published(self.items)

    @property
    def tree_path(self):
        """Return category's tree path, by his ancestors"""
        if self.parent_id:
            return '/'.join(
                [ancestor.slug for ancestor in self.get_ancestors()] +
                [self.slug])
        return self.slug

    @models.permalink
    def get_absolute_url(self):
        """Return category's URL"""
        return ('storefront_category_detail', (self.tree_path,))

    class Meta:
        """Category's Meta"""
        app_label = 'storefront'
        ordering = ['name']
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    class MPTTMeta:
        """Category MPTT's Meta"""
        order_insertion_by = ['name']
