class System:
    def __init__(self):
        self.__user_list = []
        self.__menu_list = []
        self.__payment_method = PaymentMethod()
    
    def display_menu(self):
        return [f"{menu_item.__class__.__name__}: {menu_item._Menu__name} - ${menu_item._Menu__price}" for menu_item in self.__menu_list]
    
    def select_menu(self, menu_id):
        for menu in self.__menu_list:
            if menu_id == menu.get_id():
                return menu
        return None

            
    def search_menu(self,menu_id):
        pass
            
    def add_to_cart(self, member, menu_item, quantity):
        if not menu_item:
            return "Error: Menu item not found."
        if quantity <= 0:
            return "Error: Quantity must be a positive number."
        return member.add_to_cart(menu_item, quantity)
        
    def login(self):
        pass
    
    def register(self):
        pass
    
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
    
    def logout(self):
        pass
    
    def update_profile(self):
        pass

class Member(User):
    def __init__(self, name, tel, password):
        super().__init__(name, tel, password)
        self.__order_list = []
        self.__address = None
        self.__payment = None
        self.__point = 0
        self.__coupon_list = []
        self.__cart = Cart()

    def get_cart(self):
        return self.__cart
    
    def set_cart(self, cart):
        self.__cart = cart
        
    def add_to_cart(self, menu, quantity):
        if quantity <= 0:
            return "Error: Quantity must be a positive number."
        self.__cart.add_item(menu, quantity)
        return "Success"
    

    def place_order(self):
        if not self.__cart.get_total():
            return "Error: Cart is empty!"

        total_price = self.__cart.get_total()
        print(f"Total price of cart items: ${total_price}")
        if self.__payment:
            payment_status = self.__payment.process_payment(total_price)
            if payment_status == "Success":
                order = Order(1001, self)
                order.add_item(self.__cart)
                order.calculate_total()
                self.__order_list.append(order)
                
                self.__cart.empty_cart()
                
                return "Order placed successfully!"
            else:
                return f"Payment failed: {payment_status}"
        else:
            return "Error: Payment method not set."
    
    def exchange_point_to_coupon(self):
        pass
    
    def view_order_history(self):
        pass
    
    def update_address(self,address):
        self.__address = address

class Admin(User):
    def __init__(self, name, tel, password, admin_type):
        super().__init__(name, tel, password)
        self.__type = admin_type
    
    def manage_menu(self):
        pass
    
    def view_orders(self):
        pass

class Menu:
    def __init__(self, category, menu_id, name, price, detail):
        self.__category = category
        self.__menu_id = menu_id
        self.__name = name
        self.__price = price
        self.__detail = detail
    
    def get_id(self):
        return self.__menu_id
    
    def get_details(self):
        return self
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def __str__(self):
        return self.__name
    
class Snack(Menu):
    pass

class MenuSet(Menu):
    def __init__(self, category, menu_id, name, price, detail):
        super().__init__(category, menu_id, name, price, detail)
        self.__menu_set_list = []
    
    def add_menu_item(self):
        pass
    
    def remove_menu_item(self):
        pass
    
    def get_total_price(self):
        pass

class Beverage(Menu):
    def __init__(self, category, menu_id, name, price, detail, size):
        super().__init__(category, menu_id, name, price, detail)
        self.__size = size
    
    def set_size(self, size):
        self.__size = size

class Burger(Menu):
    def __init__(self, category, menu_id, name, price, detail, addon):
        super().__init__(category, menu_id, name, price, detail)
        self.__addon = addon
    
    def add_addon(self, addon):
        self.__addon = addon
   
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

    def get_item_list(self):
        return self.__item_list
    
    def validate_cart(self):
        return len(self.__item_list) > 0
    
    def __str__(self):
        return "\n".join(str(item) for item in self.__item_list) if self.__item_list else "Cart is empty"
    
    def remove_item(self,menu):
        for item in self.__item_list:
            if item.get_menu() == menu:
                self.__item_list.remove(item)
                break
    
    def get_total(self):
        total = 0
        for item in self.__item_list:
            total += item.get_quantity() * item.get_menu().get_price()
        return round(total, 2)

class CartItem:
    def __init__(self, menu, amount):
        self.__menu = menu
        self.__amount = amount

    def get_menu(self):
        return self.__menu
    
    def add_cart_item(self,menu,amount):
        self.__menu = menu
        self.__amount = amount

    def get_detail_item(self):
        return {
            'name': self.__menu.get_name(),
            'price': self.__menu.get_price(),
            'quantity': self.__amount
        }

    
    def __str__(self):
        return f"{self.__menu.get_name()} x {self.__amount} (${self.__menu.get_price()} each)"
    
    def get_quantity(self):
        return self.__amount

    def update_quantity(self, quantity):
        """Updates the quantity of the cart item."""
        self.__amount += quantity

class Order:
    def __init__(self, order_id, member):
        self.__order_id = order_id
        self.__status = "Waiting"
        self.__member = member
        self.__total_price = 0.0
        self.__cart_items = []
        self.__payment = None
    
    def add_item(self):
        pass
    
    def remove_item(self):
        pass
    
    def calculate_total(self):
        self.__total_price = sum(item.get_quantity() * item.get_menu().get_price() for item in self.__cart_items)
        return self.__total_price

    
    def get_status(self):
        return self.__status
    
    @staticmethod
    def process_order(user):
        cart = user.get_cart()
        if cart.validate_cart():
            order = Order(1001, user)
            for item in cart.get_item_list():
                order.__cart_items.append(item)
            total = order.calculate_total()
            return f"Order placed successfully! Total: ${total:.2f}", order
        else:
            return "Error: Cart is empty or invalid", None

    
    def checkout(self):
        pass

class Address:
    def __init__(self, name, detail):
        self.__name = name
        self.__detail = detail
    
    def update_address(self):
        pass

    def get_details(self):
        return f"{self.__name}: {self.__detail}"

class Payment:
    def __init__(self, payment_id, date, total_price, status, discount, payment_method):
        self.__payment_id = payment_id
        self.__date = date
        self.__total_price = total_price
        self.__status = status
        self.__discount = discount
        self.__payment_method = payment_method
    
    def refund_payment(self):
        pass

class PaymentMethod:
    def __init__(self, payment_method_id=None, payment_method_name=None):
        self.__payment_method_id = payment_method_id
        self.__payment_method_name = payment_method_name
    
    def process_payment(self):
        pass

class QRCode(PaymentMethod):
    def __init__(self, qr_code_data):
        super().__init__()
        self.__qr_code_data = qr_code_data

class CreditCard(PaymentMethod):
    def __init__(self, card_number, expiry_date, cvv):
        super().__init__()
        self.__card_number = card_number
        self.__expiry_date = expiry_date
        self.__cvv = cvv

class Coupon:
    def __init__(self, code, discount, expire_date):
        self.__code = code
        self.__discount = discount
        self.__expire_date = expire_date

def create_mockup_instances():
    system = System()
    
    # Create admin and member users
    admin = Admin("Admin User", "123456789", "adminpass", "SuperAdmin")
    member = Member("John Doe", "987654321", "memberpass")
    
    system._System__user_list = [admin, member]
    
    # Assign an address to the member
    address = Address("John's Home", "123 Street, City, Country")
    member.update_address(address)
    
    # Create menu items
    burger = Burger("Fast Food", 1, "Cheese Burger", 5.99, "Delicious cheeseburger", "Extra Cheese")
    drink = Beverage("Beverage", 2, "Coke", 1.99, "Refreshing drink", "Medium")
    snack = Snack("Snacks", 3, "French Fries", 2.99, "Crispy and golden")
    
    menu_set = MenuSet("Combo", 4, "Burger Combo", 9.99, "Burger with fries and drink")
    menu_set.add_menu_item = [burger, drink, snack]
    
    system._System__menu_list = [burger, drink, snack, menu_set]

    cart = member.get_cart()
    cart.add_item(burger, 1)
    cart.add_item(drink, 2)
    cart.add_item(snack, 2)
   
    return {
        "system": system,
        "admin": admin,
        "member": member,
        "address": address,
        "menu_items": [burger, drink, snack],
        "menu_set": menu_set,
        "cart": cart,
        
    }

# Example usage
def watch_cart_and_checkout(system, member):
    print("Cart Contents:")
    print(member.get_cart())

    print("\nAttempting to checkout...")
    result = member.place_order()
    print(f"Checkout result: {result}")

    if "Order placed successfully!" in result:
        print("\nOrder was successful!")
    else:
        print("\nOrder failed. Please check the issue.")

# Example usage with mockup data
mockup_data = create_mockup_instances()

watch_cart_and_checkout(mockup_data["system"], mockup_data["member"])