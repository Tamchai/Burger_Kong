# System Implementation

class System:
    def __init__(self):
        self.__user_list = []
        self.__menu_list = []
        self.__payment_method = PaymentMethod()
        self.__cart = Cart()
    def get_total_price(self):
        return self.__cart.get_total()
    def display_menu(self):
        return [f"{menu_item.__class__.__name__}: {menu_item.get_name()} - ${menu_item.get_price()}" for menu_item in self.__menu_list]

    def select_menu(self, menu_id):
        for menu in self.__menu_list:
            if menu_id == menu.get_id():
                return menu
        return None

    def add_to_cart(self, member, menu_item, quantity):
        if not menu_item:
            return "Error: Menu item not found."
        if quantity <= 0:
            return "Error: Quantity must be a positive number."
        return member.add_to_cart(menu_item, quantity)

    def search_user_by_id(self, user_id):
        for user in self.__user_list:
            if user.get_id() == user_id:
                return user
        return None


class User:
    def __init__(self, name, tel, password):
        self.__name = name
        self.__tel = tel
        self.__password = password

class Member(User):
    def __init__(self, name, tel, password):
        super().__init__(name, tel, password)
        self.__order_list = []
        self.__address = None
        self.__payment = None
        self.__cart = Cart()

    def get_cart(self):
        return self.__cart

    def add_to_cart(self, menu, quantity):
        return self.__cart.add_item(menu, quantity)

    def place_order(self):
        total_price = System.get_total_price
        if not self.__cart.validate_cart():
            return "Error: Cart is empty!"

        
        if self.__payment:
            payment_status = self.__payment.process_payment(total_price)
            if payment_status == "Payment Successful via Credit Card":
                order = Order(1001, self.__cart)
                self.__order_list.append(order)
                self.__cart.empty_cart()
                return "Order placed successfully!"
            else:
                return f"Payment failed: {payment_status}"
        else:
            return "Error: Payment method not set."

    def set_payment_method(self, payment_method):
        self.__payment = payment_method


class Menu:
    def __init__(self, menu_id, name, price):
        self.__menu_id = menu_id
        self.__name = name
        self.__price = price

    def get_id(self):
        return self.__menu_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class Cart:
    def __init__(self):
        self.__item_list = []

    def add_item(self, menu, quantity):
        for item in self.__item_list:
            if item.get_menu() == menu:
                item.update_quantity(quantity)
                return "Item quantity updated in cart."
        new_item = CartItem(menu, quantity)
        self.__item_list.append(new_item)
        return "Item added to cart."

    def validate_cart(self):
        return len(self.__item_list) > 0

    def get_total(self):
        return round(sum(item.get_quantity() * item.get_menu().get_price() for item in self.__item_list), 2)

    def empty_cart(self):
        self.__item_list = []


class CartItem:
    def __init__(self, menu, quantity):
        self.__menu = menu
        self.__quantity = quantity

    def get_menu(self):
        return self.__menu

    def get_quantity(self):
        return self.__quantity

    def update_quantity(self, quantity):
        self.__quantity += quantity


class Order:
    def __init__(self, order_id, cart):
        self.__order_id = order_id
        self.__cart = cart
        self.__total_price = cart.get_total()

    def get_total_price(self):
        return self.__total_price


class PaymentMethod:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement process_payment method")


class CreditCard(PaymentMethod):
    def __init__(self, card_number, expiry_date, cvv):
        self.__card_number = card_number
        self.__expiry_date = expiry_date
        self.__cvv = cvv

    def process_payment(self, amount):
        return "Payment Successful via Credit Card"


# Function to create mock data for testing
def create_mockup_instances():
    system = System()

    # Create a member user
    member = Member("John Doe", "987654321", "memberpass")
    system._System__user_list = [member]

    # Create menu items
    burger = Menu(1, "Cheese Burger", 5.99)
    drink = Menu(2, "Coke", 1.99)
    snack = Menu(3, "French Fries", 2.99)

    system._System__menu_list = [burger, drink, snack]

    cart = member.get_cart()
    cart.add_item(burger, 1)
    cart.add_item(drink, 2)

    return {
        "system": system,
        "member": member,
        "menu_items": [burger, drink, snack],
        "cart": cart,
    }


# Test Cases
def test_system():
    print("\n=== Running System Tests ===")

    # Create mockup instances
    data = create_mockup_instances()
    system = data["system"]
    member = data["member"]
    cart = member.get_cart()

    # Test adding items to cart
    print("\n--- Test: Adding items to cart ---")
    burger, drink, snack = data["menu_items"]
    cart.add_item(snack, 1)
    print("Cart after adding items:", cart.get_total())

    # Test removing an item from cart
    print("\n--- Test: Removing an item from cart ---")
    cart.empty_cart()
    print("Cart after emptying:", cart.get_total())

    # Test cart total calculation
    print("\n--- Test: Cart total calculation ---")
    cart.add_item(burger, 1)
    expected_total = round(burger.get_price(), 2)
    cart_total = cart.get_total()
    print(f"Expected Total: ${expected_total}, Calculated Total: ${cart_total}")
    print("Total price test passed:", cart_total == expected_total)

    # Test placing order without setting a payment method
    print("\n--- Test: Placing order without payment method ---")
    result = member.place_order()
    print("Order Result:", result)

    # Test setting a payment method and placing an order
    print("\n--- Test: Placing order with payment method ---")
    member.set_payment_method(CreditCard("1234567812345678", "12/26", "123"))
    result = member.place_order()
    print("Order Result:", result)

    # Test order history
    print("\n--- Test: Viewing order history ---")
    print("Order history length:", len(member._Member__order_list))


# Run the test
test_system()
