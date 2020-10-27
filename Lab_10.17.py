# Andrew Li
# 1824794

class ItemToPurchase:
    def __init__(self, name="none", item_price=0, item_quantity=0):
        self.name = name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print("{} {} @ ${:.0f} = ${:.0f}".format(self.name, self.item_quantity, self.item_price, total))


print("Item 1")
item1_name = input("Enter the item name:\n")
item1_price = float(input("Enter the item price:\n"))
item1_quantity = int(input("Enter the item quantity:\n"))
item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)
print()
print("Item 2")
item2_name = input("Enter the item name:\n")
item2_price = float(input("Enter the item price:\n"))
item2_quantity = int(input("Enter the item quantity:\n"))
item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)

print("TOTAL COST")
item1.print_item_cost()
item2.print_item_cost()
