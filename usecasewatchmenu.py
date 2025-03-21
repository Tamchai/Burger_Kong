class System:
    
    def __init__(self):
        self.__user_list = []
        self.__menu_list = []
        self.__payment_method = PaymentMethod()
    # def display_menu(self):
    #     return self.__menu_list
    def display_menu(self):
        return [f"{menu_item.__class__.__name__}: {menu_item._Menu__name} - ${menu_item._Menu__price}" for menu_item in self.__menu_list]
    def select_menu(self,menu_id):
        for menus in self.__menu_list:
            if menu_id == menus.get_id():
                return menus
        pass
    def search_menu(self,menu_name):
        search_list = []
        for menus in self.__menu_list:
            if menu_name in menus.get_name():
                search_list.append(menus)
        return [menu.get_details() for menu in search_list]

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
        self.__cart = Cart()
    def get_cart(self):
        return self.__cart
    def set_cart(self, cart):
        self.__cart = cart
        
    def add_to_cart(self, menu, quantity):
        if quantity <= 0:
            return "Error: Quantity must be a positive number."
        self.__cart.add_item(menu, quantity)
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
    
    def get_id(self):
        return self.__menu_id
    def get_details(self):
        return [self.__name,self.__price,self.__detail]
    def get_name(self):
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
    # def __str__(self):
    #     return f'id : {self.get_id()}'

class Cart:
    def __init__(self):
        self.__item_list = []
    
    def add_item(self, menu, quantity):
        for item in self.__item_list:
            if item.get_menu() == menu:
                item.update_quantity(quantity)  # Update quantity if item exists
                return
        new_item = CartItem(menu, quantity)
        self.__item_list.append(new_item)  # Add new item to cart
    
    def __str__(self):
        return "\n".join(str(item) for item in self.__item_list) if self.__item_list else "Cart is empty"
    
    
    
    def remove_item(self):
        pass
    
    def get_total(self):
        pass

class CartItem:
    def __init__(self, menu, amount):
        self.__menu = menu
        self.__amount = amount
    def get_menu(self):
        return self.__menu
    
    def __str__(self):
        return f"{self.__menu.get_details()[0]} x {self.__amount} (${self.__menu.get_details()[1]} each)"

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
    system = System()
    
    # Create admin and member users
    admin = Admin("Admin User", "123456789", "adminpass", "SuperAdmin")
    member = Member("John Doe", "987654321", "memberpass")
    
    system._System__user_list = [admin, member]
    
    # Assign an address to the member
    address = Address("John's Home", "123 Street, City, Country")
    member.update_address = address
    
    # Create menu items
    burger = Burger("Fast Food", 1, "Cheese Burger", 5.99, "Delicious cheeseburger", "Extra Cheese")
    drink = Beverage("Beverage", 2, "Coke", 1.99, "Refreshing drink", "Medium")
    snack = Snack("Snacks", 3, "French Fries", 2.99, "Crispy and golden")
    
    menu_set = MenuSet("Combo", 4, "Burger Combo", 9.99, "Burger with fries and drink")
    menu_set.add_menu_item = [burger, drink, snack]
    
    system._System__menu_list = [burger, drink, snack, menu_set]

    # Use the member's own cart
    cart = member.get_cart()
    # cart_item1 = CartItem(burger, 2)
    # cart_item2 = CartItem(drink, 1)
    # cart_item3 = CartItem(snack, 1)
    # cart.add_item(cart_item1.get_menu(), cart_item1.get_quantity())
    # cart.add_item(cart_item2.get_menu(), cart_item2.get_quantity())
    # cart.add_item(cart_item3.get_menu(), cart_item3.get_quantity())


    # Create order linked to the member
    # order = Order(1001, member)
    # order.add_item = [cart_item1, cart_item2, cart_item3]
    # order.calculate_total = 15.96

    # qr_payment = QRCode("QR_DATA_12345")
    # credit_payment = CreditCard("1234567890123456", "12/25", "123")

    # payment = Payment(5001, "2025-02-13", order.calculate_total, "Completed", 2.0, qr_payment)

    # coupon = Coupon("SAVE10", 10, "2025-12-31")
    # member.exchange_point_to_coupon = [coupon]

    print(system.display_menu())
    selectedmenu = system.select_menu(2)
    print(selectedmenu.get_details())
    member.set_cart(cart)
    member.add_to_cart(selectedmenu,2)
    selectedmenu = system.select_menu(4)
    member.add_to_cart(selectedmenu,10)
    print(member.get_cart())
    
    print(system.search_menu("B"))
    return {
        "system": system,
        "admin": admin,
        "member": member,
        "address": address,
        "menu_items": [burger, drink, snack],
        "menu_set": menu_set,
        "cart": cart,
        # "order": order,
        # "payment_methods": [qr_payment, credit_payment],
        # "payment": payment,
        # "coupon": coupon,
    }

# Example usage
mockup_data = create_mockup_instances()


