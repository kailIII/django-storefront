from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from storefront.settings import DEFAULT_CURRENCY

class BaseCart(models.Model):

    # If the user is null, that means this is used for a session
    user = models.OneToOneField(User, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta(object):
        abstract = True
        app_label = 'storefront'
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')

    def __init__(self, *args, **kwargs):
        super(BaseCart, self).__init__(*args, **kwargs)
        # That will hold things like tax totals or total discount
        self.subtotal_price = Decimal('0.0')
        self.total_price = Decimal('0.0')
        self.current_total = Decimal('0.0') # used by cart modifiers
        self.extra_price_fields = [] # List of tuples (label, value)
        self._updated_cart_items = None

    def add_product(self, product, quantity=1, merge=True, queryset=None):

        from shop.models import CartItem

        # check if product can be added at all
        if not getattr(product, 'can_be_added_to_cart', True):
            return None

        # get the last updated timestamp
        # also saves cart object if it is not saved
        self.save()

        if queryset is None:
            queryset = CartItem.objects.filter(cart=self, product=product)
        item = queryset
        # Let's see if we already have an Item with the same product ID
        if item.exists() and merge:
            cart_item = item[0]
            cart_item.quantity = cart_item.quantity + int(quantity)
            cart_item.save()
        else:
            cart_item = CartItem.objects.create(
                cart=self, quantity=quantity, product=product)
            cart_item.save()

        return cart_item

    def update_quantity(self, cart_item_id, quantity):
        """
        Updates the quantity for given cart item or deletes it if its quantity
        reaches `0`
        """
        cart_item = self.items.get(pk=cart_item_id)
        if quantity == 0:
            cart_item.delete()
        else:
            cart_item.quantity = quantity
            cart_item.save()
        self.save()
        return cart_item

    def delete_item(self, cart_item_id):
        """
        A simple convenience method to delete one of the cart's items. This
        allows to implicitely check for "access rights" since we insure the
        cartitem is actually in the user's cart
        """
        cart_item = self.items.get(pk=cart_item_id)
        cart_item.delete()
        self.save()

    def get_updated_cart_items(self):
        """
        Returns updated cart items after update() has been called and
        cart modifiers have been processed for all cart items.
        """
        assert self._updated_cart_items is not None, ('Cart needs to be '
            'updated before calling get_updated_cart_items.')
        return self._updated_cart_items

    def update(self, state=None):
        """
        This should be called whenever anything is changed in the cart (added
        or removed).
        It will loop on all line items in the cart, and call all the price
        modifiers on each row.
        After doing this, it will compute and update the order's total and
        subtotal fields, along with any payment field added along the way by
        modifiers.

        Note that theses added fields are not stored - we actually want to
        reflect rebate and tax changes on the *cart* items, but we don't want
        that for the order items (since they are legally binding after the
        "purchase" button was pressed)
        """

        # This is a ghetto "select_related" for polymorphic models.
        items = CartItem.objects.filter(cart=self)
        product_ids = [item.product_id for item in items]
        products = Product.objects.filter(pk__in=product_ids)
        products_dict = dict([(p.pk, p) for p in products])

        self.extra_price_fields = [] # Reset the price fields
        self.subtotal_price = Decimal('0.0') # Reset the subtotal

        # This will hold extra information that cart modifiers might want to
        # pass to each other
        if state is None:
            state = {}

        # This calls all the pre_process_cart methods (if any), before the cart
        # is processed. This allows for data collection on the cart for
        # example)
        for modifier in cart_modifiers_pool.get_modifiers_list():
            modifier.pre_process_cart(self, state)

        for item in items: # For each CartItem (order line)...
            # This is still the ghetto select_related
            item.product = products_dict[item.product_id]
            self.subtotal_price = self.subtotal_price + item.update(state)

        self.current_total = self.subtotal_price
        # Now we have to iterate over the registered modifiers again
        # (unfortunately) to pass them the whole Order this time
        for modifier in cart_modifiers_pool.get_modifiers_list():
            modifier.process_cart(self, state)

        self.total_price = self.current_total

        # This calls the post_process_cart method from cart modifiers, if any.
        # It allows for a last bit of processing on the "finished" cart, before
        # it is displayed
        for modifier in cart_modifiers_pool.get_modifiers_list():
            modifier.post_process_cart(self, state)

        # Cache updated cart items
        self._updated_cart_items = items

    def empty(self):
        """ Remove all cart items """
        if self.pk:
            self.items.all().delete()
            self.delete()

    @property
    def total_quantity(self):
        """ Returns the total quantity of all items in the cart """
        return sum([ci.quantity for ci in self.items.all()])



class Cart(BaseCart):
    class Meta(object):
        abstract = False
        app_label = 'storefront'
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')
