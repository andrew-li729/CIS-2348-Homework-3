# Andrew Li
# 1824794

class ItemToPurchase:
    def __init__(self, name="none", item_price=0, item_quantity=0):
        self.name = name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(total)


item1 = ItemToPurchase()
item1.print_item_cost()
