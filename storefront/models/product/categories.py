"""Category model for storefront"""
from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField(blank=True)
    meta_description = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True)
    related = models.ManyToManyField('self', blank=True, null=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        verbose_name='parent category',
        related_name='children', )

    class Meta:
        app_label = 'storefront'
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('storefront:category_detail', kwargs={'slug':self.slug})
