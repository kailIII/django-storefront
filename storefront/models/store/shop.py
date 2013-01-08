from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _

from storefront.models.l10n.country import Country

class Config(models.Model):
    """
    Used to store specific information about the store.
    Also used to configure various store behaviour.
    """
    
    #site = models.OneToOneField(Site, verbose_name=_("Site"), primary_key=True)
    store_name = models.CharField(_("Store Name"),max_length=100, unique=True)
    store_description = models.TextField(_("Description"), blank=True, null=True)
    store_email = models.EmailField(_("Email"), blank=True, null=True, max_length=75)
    street1=models.CharField(_("Street"),max_length=50, blank=True, null=True)
    city=models.CharField(_("City"), max_length=50, blank=True, null=True)
    state=models.CharField(_("State"), max_length=30, blank=True, null=True)
    postal_code=models.CharField(_("Zip Code"), blank=True, null=True, max_length=9)
    country=models.ForeignKey(Country, blank=False, null=False, verbose_name=_('Country'))
    phone = models.CharField(_("Phone Number"), blank=True, null=True, max_length=30)
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
        
    def __unicode__(self):
        return self.store_name
        
    class Meta:
        verbose_name = _("Store Configuration")
        verbose_name_plural = _("Store Configurations")
        app_label = 'storefront'
