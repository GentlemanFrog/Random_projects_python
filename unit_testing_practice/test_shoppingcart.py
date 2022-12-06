from shoppingcart import ShoppingCart
import pytest

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
    for i in range(5):
        cart.add_item_to_list('Cans')
    
    '''This line I expect that code below this lane raises
    this type of error, if it does then the pytest will pass it.
    In this form of the test i exactly know that it raises on the
    6th item which is out of max range'''
    with pytest.raises(OverflowError):
        cart.add_item_to_list('Cans')
        
def test_total_price_from_items_in_cart():
    cart = ShoppingCart(5)
    cart.add_item_to_list('Banana')
    cart.add_item_to_list('Beans')
    cart.add_item_to_list('Cans')
    
    price_map = {
        "Banana": 2.0,
        "Beans": 3.0,
        "Cans": 5.0
    }
    
    '''Total price of the items we add should be equal
    to 10.0 '''
    assert cart.get_total_price(price_map) == 10.0