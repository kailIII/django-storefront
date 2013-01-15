from storefront.models.product.categories import Category
from storefront.models.product.items import Item
from storefront.models.frontend.banners import Banner

from storefront.forms import ContactForm

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from storefront.settings import COMPANY_INFO

from django.core.mail import send_mail

class HomePage( TemplateView ):
    
    template_name="storefront/home.html"
	
    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['feature_list'] = Item.objects.filter(featured=True)
        context['category_list'] = Category.objects.all()
        context['banner_list'] = Banner.objects.all()
        return context


class AboutPage( TemplateView ):
    
    template_name="storefront/about.html"
	
    def get_context_data(self, **kwargs):
        context = super(AboutPage, self).get_context_data(**kwargs)
        return context
        
class ContactPage( FormView ):
    
    template_name="storefront/contact.html"
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        cc_myself = form.cleaned_data['cc_myself']
        recipients = [COMPANY_INFO['email']]
        if cc_myself:
            recipients.append(sender)

        send_mail(subject, message, sender, recipients)
        return super(ContactPage, self).form_valid()

            

    
