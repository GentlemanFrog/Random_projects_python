# shoping cart script
from typing import List 

class ShoppingCart:
    def __init__(self) -> None:
        self.items: List[str] = []
    
    def add_item_to_list(self, item: str):
        self.items.append(item)
    
    def size(self) -> int:
        return 0
    
    def get_item(self)-> List[str]:
        pass
    
    def get_total_price(self, price_map):
        pass
    
    