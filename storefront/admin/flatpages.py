from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.admin import FlatpageForm

from storefront.settings import FLATPAGE_TEMPLATE_CHOICES

from django import forms

class MyFlatpageForm(FlatpageForm):
    template = forms.ChoiceField(choices=FLATPAGE_TEMPLATE_CHOICES)

class MyFlatPageAdmin(FlatPageAdmin):
    form = MyFlatpageForm
