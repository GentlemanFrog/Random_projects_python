from shoppingcart import ShoppingCart

def test_can_add_item_to_cart():
    # making instance of class to test it:
    cart = ShoppingCart(5)
    cart.add_item_to_list('beans')
    
    '''to check that apple was added the size was checked
    assert should throw exception if condtition is not met'''
    assert cart.size() == 1
    
def test_when_item_added_and_list_contains_it():
    cart = ShoppingCart(5)
    cart.add_item_to_list('beans')
    
    '''Checking the condition if added item is in list containing
    all items'''
    assert 'beans' in cart.get_items()

def test_to_check_overflow_of_list_with_fixed_range():
    cart = ShoppingCart(5)
    
    '''By adding 6 items we want it to fail, if anothre value
    is in cart change it to check it its working'''
    for i in range(6):
        cart.add_item_to_list('Cans')
        