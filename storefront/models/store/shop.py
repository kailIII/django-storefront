class OrderCart():
    """
    Used to keep a persistant cart for each user.
    Currently not sure whether or not to store in DB or not.
    """
    numberItems
    totalCost
    itemlist #This should be a tuple list, item+amount
    

class OrderHistory():
    """
    Used to keep track of what users bought to bring up a custom display of their fav items.
    """

    ORDER_CHOICES=( 'Online','inPerson', 'show',)
    ORDER_STATUS=('Queued', 'New', 'Blocked', 'In Process', 'Billed', 'Shipped', 'Complete', 'Cancelled',)
