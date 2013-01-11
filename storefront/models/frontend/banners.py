from django.db import models
from django.utils.translation import ugettext_lazy as _

class Banner(models.Model):
    """
    Banner to be displayed on the main page.
    If the user creates more than one they will be played through as a slide show.
    The Duration of each slide is to be controlled via STOREFRONT_SETTINGS. (NOT HERE)
    """
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
        verbose_name = _("Bannner Image")
        verbose_name_plural = _("Banner Images")
