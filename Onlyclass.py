class System:
    def __init__(self):
        self.__user_list = []
        self.__menu_list = []
        self.__payment_method = PaymentMethod()
    
    def search_menu(self):
        pass
    
    def login(self):
        pass
    
    def register(self):
        pass

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
    
    def place_order(self):
        pass
    
    def exchange_point_to_coupon(self):
        pass
    
    def view_order_history(self):
        pass
    
    def update_address(self):
        pass

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
    
    def get_details(self):
        pass

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
    
    def add_item(self):
        pass
    
    def remove_item(self):
        pass
    
    def get_total(self):
        pass

class CartItem:
    def __init__(self, menu, amount):
        self.__menu = menu
        self.__amount = amount

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
        pass
    
    def checkout(self):
        pass

class Address:
    def __init__(self, name, detail):
        self.__name = name
        self.__detail = detail
    
    def update_address(self):
        pass

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
    # Create system instance
    system = System()
    
    # Create admin and member users
    admin = Admin("Admin User", "123456789", "adminpass", "SuperAdmin")
    member = Member("John Doe", "987654321", "memberpass")
    
    # Add users to system
    system._System__user_list = [admin, member]
    
    # Create address instance
    address = Address("John's Home", "123 Street, City, Country")
    member.update_address = address
    
    # Create menu items
    burger = Burger("Fast Food", 1, "Cheese Burger", 5.99, "Delicious cheeseburger", "Extra Cheese")
    drink = Beverage("Beverage", 2, "Coke", 1.99, "Refreshing drink", "Medium")
    snack = Snack("Snacks", 3, "French Fries", 2.99, "Crispy and golden")
    
    # Create menu set
    menu_set = MenuSet("Combo", 4, "Burger Combo", 9.99, "Burger with fries and drink")
    menu_set.add_menu_item = [burger, drink, snack]
    
    # Add menu items to system
    system._System__menu_list = [burger, drink, snack, menu_set]
    
    # Create cart and add items
    cart = Cart()
    cart_item1 = CartItem(burger, 2)
    cart_item2 = CartItem(drink, 1)
    cart_item3 = CartItem(snack, 1)
    cart.add_item = [cart_item1, cart_item2, cart_item3]
    
    # Create order
    order = Order(1001, member)
    order.add_item = [cart_item1, cart_item2, cart_item3]
    order.calculate_total = 15.96
    
    # Create payment methods
    qr_payment = QRCode("QR_DATA_12345")
    credit_payment = CreditCard("1234567890123456", "12/25", "123")
    
    # Create payment
    payment = Payment(5001, "2025-02-13", order.calculate_total, "Completed", 2.0, qr_payment)
    
    # Create coupon
    coupon = Coupon("SAVE10", 10, "2025-12-31")
    member.exchange_point_to_coupon = [coupon]
    
    return {
        "system": system,
        "admin": admin,
        "member": member,
        "address": address,
        "menu_items": [burger, drink, snack],
        "menu_set": menu_set,
        "cart": cart,
        "order": order,
        "payment_methods": [qr_payment, credit_payment],
        "payment": payment,
        "coupon": coupon,
    }

# Example usage
mockup_data = create_mockup_instances()
print(mockup_data)

