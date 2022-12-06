from shoppingcart import ShoppingCart

def test_can_add_item_to_cart():
    # making instance of class to test it:
    cart = ShoppingCart()
    cart.add_item_to_list('beans')
    
    '''to check that apple was added the size was checked
    assert should throw exception if condtition is not met'''
    assert cart.size() == 1
    
    
    
