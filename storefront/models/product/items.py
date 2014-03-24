from django.db import models
from django.core.urlresolvers import reverse
from storefront.models.product.categories import Category

 
class Item(models.Model):
    name = models.CharField( max_length=255, )
    slug = models.SlugField( unique=True, max_length=255)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    categories = models.ManyToManyField(Category, blank=True, null=True)
    amount_in_stock = models.IntegerField(default=0)
    meta_description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    comment_enabled = models.BooleanField(default=True)
    is_on_sale = models.BooleanField(default=False)
    start_sale = models.DateTimeField(blank=True, null=True)
    end_sale = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'storefront'

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('storefront:item_detail', kwargs={'slug':self.slug})

    
class ItemImage(models.Model):
    item = models.ForeignKey(Item)
    picture = models.ImageField(upload_to="images/", blank=True, null=True)
    caption = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        if self.caption:
            return "%s" % self.caption
        else:
            return "%s" % self.picture

    class Meta:
        app_label = 'storefront'

 



