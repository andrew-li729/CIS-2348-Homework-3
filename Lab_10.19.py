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
    def __init__(self, customer_name="none", current_date="January 1, 2016", cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

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

    def modify_item(self):
        item_string = input("Enter the item name:\n")
        for item in self.cart_items:
            if item_string == item.item_name:
                new_quantity = int(input("Enter the new quantity:\n"))
                item.item_quantity = new_quantity
                break
            else:
                print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_num_items = 0
        for item in self.cart_items:
            num_items = item.item_quantity
            total_num_items += num_items
        return total_num_items

    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            cost = item.item_price * item.item_quantity
            total += cost
        return total

    def print_total(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Number of items: {}\n".format(self.get_num_items_in_cart()))
        for item in self.cart_items:
            print("{} {} @ ${:.0f} = ${:.0f}".format(item.item_name, item.item_quantity, item.item_price,
                                                     item.item_price * item.item_quantity))
        print()
        print("Total: ${}".format(self.get_cost_of_cart()))

    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Item Descriptions")
        for item in self.cart_items:
            print("{}: {}".format(item.item_name, item.item_description))


if __name__ == '__main__':
    # initialize and print customer name and date
    name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    print()
    print("Customer name:", name)
    print("Today's date:", date)

    # create ShoppingCart object
    cart1 = ShoppingCart(customer_name=name, current_date=date)


    def print_menu(cart):
        command = ""
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit\n")
        while command != "q":
            command = input("Choose an option:")
            while (command != 'a' and command != 'o' and command != 'i' and command != 'r'
                   and command != 'c' and command != 'q'):
                command = input('Choose an option: ')
            if command == 'a':
                cart.add_item()
            if command == "r":
                cart.remove_item()
            if command == "c":
                cart.modify_item()
            if command == "i":
                print("OUTPUT ITEMS' DESCRIPTIONS")
                cart.print_descriptions()
            if command == "o":
                print("OUTPUT SHOPPING CART")
                cart.print_total()


    print_menu(cart1)
