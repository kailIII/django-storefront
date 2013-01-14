from storefront.models.product.categories import Category
from storefront.models.product.items import Item
from storefront.models.frontend.banners import Banner

from django.views.generic.base import TemplateView

#for contact form only
from django.shortcuts import render
from django.http import HttpResponseRedirect

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
    
    #queryset = ''
	
    def get_context_data(self, **kwargs):
        context = super(AboutPage, self).get_context_data(**kwargs)
        return context
        
class ContactPage( TemplateView ):
    
    template_name="storefront/contact.html"
    
    def contact(request):
        if request.method == 'POST': # If the form has been submitted...
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                sender = form.cleaned_data['sender']
                cc_myself = form.cleaned_data['cc_myself']
                
                recipients =['COMPANY_EMAIL'] #GET THIS FROM SETTINGS!!!
                if cc_myself:
                    recipients.append(sender)
                    
                from django.core.mail import send_mail
                send_mail(subject, message, sender, recipients)
                return HttpResponseRedirect('/thanks/')
        else:
            form = ContactForm()
        return render(request, 'storefront/contact.html', {
                'form': form,
        })
            
    def get_context_data(self, **kwargs):
        context = super(ContactPage, self).get_context_data(**kwargs)
        return context
