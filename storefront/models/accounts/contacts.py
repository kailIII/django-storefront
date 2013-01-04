#from django.db import models
#
#class Contact(models.Model):
#    """
#    A customer, supplier, or any entity that a store owner might interact with
#    """
#
#    title = models.CharField()
#    name = models.CharField()
#    user = models.CharField()
#    role = models.	#
#    orginization = models.Foreignkey(Organization)
#    email = models.
#    phone = models.
#    address = models. #See address book, use foreign key unique id's here
#    notes = models.TextField()
#   
#class Organization(models.Model):
#    """
#    An organization can be a company, government or any kind of group.
#    """
#
#    name = models.CharField()
#    type = models.CharField()
#    role = models.
#    notes = models.TextField()
#
#class Address(models.Model):
#    """
#    Address information.
#    """
#
#    contact = models.Foreignkey(Contact) # Reverse lookup
#    description = models.CharField() #Home, office, warehouse...
#    addressee = models.CharField() # Person Name
#    street = models.CharField()
#    city = models.CharField()
#    locality = models.CharField()#State, Province, Territory
#    country = models.CharField()
#    is_default_billing = models.BooleanField()
#    is_default_shipping = models.BooleanField()

