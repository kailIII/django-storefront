from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _

from storefront.models.l10n.country import Country

class Config(models.Model):

    country=models.ForeignKey(Country, blank=False, null=False, verbose_name=_('Country'))
    in_country_only = models.BooleanField(
        _("Only sell to in-country customers?"),
        default=True)
    sales_country = models.ForeignKey(
        Country, blank=True, null=True,
        related_name='sales_country',
        verbose_name=_("Default country for customers"))
    shipping_countries = models.ManyToManyField(
        Country,
        blank=True,
        verbose_name=_("Shipping Countries"),
        related_name="shop_configs")
        
    #def __unicode__(self):
    #    return self.store_name
        
    class Meta:
        verbose_name = _("Store Configuration")
        verbose_name_plural = _("Store Configurations")
        app_label = 'storefront'
