"""Forms for storefront admin"""

from django import forms
#from django.db.models. import manyToOneRel

from storefront.models.products import Category, Product

class CategoryAdminForm(forms.ModelForm):
    """Form for Category's Admin"""
    class Meta:
        """CategoryAdminForm's Meta"""
        model = Category

class ProductAdminForm(forms.ModelForm):
    """Form for Product's Admin"""
    class Meta:
        """ProductAdminForm's Meta"""
        model = Product
