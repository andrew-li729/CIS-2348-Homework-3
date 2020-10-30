# Andrew Li
# 1824794

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print("{} {} @ ${:.0f} = ${:.0f}".format(self.item_name, self.item_quantity, self.item_price,
                                                 self.item_price * self.item_quantity))

    def print_item_description(self):
        print(self.item_description)

    def compute_total(self):
        return self.item_price * self.item_quantity


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self):
        print('ADD ITEM TO CART')
        item_name = str(input('Enter the item name:\n'))
        item_description = str(input('Enter the item description:\n'))
        item_price = int(input('Enter the item price:\n'))
        item_quantity = int(input('Enter the item quantity:\n'))

        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))

    def remove_item(self):
        item_string = input("Enter name of item to remove:\n")
        for item in self.cart_items:
            if item_string == item.item_name:
                del self.cart_items[self.cart_items.index(item)]
                break
            else:
                print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase):
        item_string = ItemToPurchase
        new_quantity = int(input("Enter the new quantity:\n"))
        flag = None
        for item in self.cart_items:
            if item_string == item.item_name:
                item.item_quantity = new_quantity
                flag = True
                break
            else:
                flag = False
        if not flag:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            cost = item.item_price * item.item_quantity
            total += cost
        return total

    def print_total(self):
        if not self.cart_items:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("Number of Items: {}\n".format(self.get_num_items_in_cart()))
            print("SHOPPING CART IS EMPTY\n")
            print("Total: ${}".format(self.get_cost_of_cart()))

        else:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("Number of Items: {}\n".format(self.get_num_items_in_cart()))
            for item in self.cart_items:
                print("{} {} @ ${:.0f} = ${:.0f}".format(item.item_name, item.item_quantity, item.item_price,
                                                         item.item_price * item.item_quantity))
            print()
            print("Total: ${}".format(self.get_cost_of_cart()))

    def print_descriptions(self):
        print("{}'s Shopping Cart - {}\n".format(self.customer_name, self.current_date))
        print("Item Descriptions")
        for item in self.cart_items:
            print("{}: {}".format(item.item_name, item.item_description))


def print_menu(cart):
    option = ""
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit\n")

    while option != 'a' and option != 'o' and option != 'i' and option != 'r' and option != 'c' and option != 'q':
        option = input('Choose an option:\n')
    if option == 'a':
        cart.add_item()
    if option == "r":
        cart.remove_item()
    if option == "c":
        print("CHANGE ITEM QUANTITY")
        cart.modify_item(input("Enter item name:"))
    if option == "i":
        print("OUTPUT ITEMS' DESCRIPTIONS")
        cart.print_descriptions()
    if option == "o":
        print("OUTPUT SHOPPING CART")
        cart.print_total()
    return option


if __name__ == '__main__':
    # initialize and print customer name and date
    name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    print()
    print("Customer name:", name)
    print("Today's date:", date)
    option = ""
    # create ShoppingCart object
    cart1 = ShoppingCart(customer_name=name, current_date=date)
    while option != "q":
        print("")
        option = print_menu(cart1)
