django-storefront
=================

Storefront takes code ideas and structure from the following projects.

* Zinnia
* Satchmo

I do not intend this to be a framework that can be heavily customized, but rather a complete solution.
The one thing I will leave as to be added in is payment methods. Unitl I feel comfortable with taking online payment, this functionality will appear as order forms/requests, without actual payment processing.

Required Dependencies at the moment
----------------------------
* django-mptt
* django version 1.4 or better

ToDo:
---------------------------------
* The admin is still very plain but at least it is fully functional.
    * Customize to make product and store configuration even easier.
    
* There were some problems with comments appearing on every product, instead of sticking to an individual item.
    * Add comments back in.
    
* There is no pricing yet. ( Models + Template + View )
* There is no cart yet. ( Models + Template + View )
* There is no backward navigation/breadcrums yet. ( Template + Views )
* Write up Documentation.
* Write up Tests.
