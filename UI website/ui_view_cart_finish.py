from fasthtml.common import *
from dataclasses import dataclass

app, rt = fast_app(live=True)
class System:
    def __init__(self):
        self.__user_list = []
        self.__menu_list = []
        self.__payment_method = PaymentMethod()
    
    def display_menu(self):
        return [f"{menu_item.__class__.__name__}: {menu_item._Menu__name} - ${menu_item._Menu__price}" for menu_item in self.__menu_list]
            
    def select_menu(self,menu_id):
        menu = self.search_menu_by_id(menu_id)
        return menu
    def get_usr_list(self):
        return self.__user_list
    def search_menu_by_id(self,menu_id):
        for menus in self.__menu_list:
            if menu_id == menus.get_id():
                return menus

    def search_user_by_id(self,user_id):
        for users in self.__user_list:
            if users.get_id() == user_id:
                return users
            
    def add_to_cart(self, user_id, menu_item, quantity, addons=None):
        member = self.search_user_by_id(user_id)
        if not menu_item:
            return "Error: Menu item not found."
        if quantity <= 0:
            return "Error: Quantity must be a positive number."

        total_price = menu_item.get_price() * quantity

        if isinstance(addons, str):  
            addons = [addons]
        elif addons is None or not isinstance(addons, (list, tuple)):  
            addons = []

        if isinstance(menu_item, Burger) and addons:
            for addon in addons:
                if addon in menu_item.get_addons():
                    total_price += menu_item.get_addons()[addon] * quantity

        return member.add_to_cart(menu_item, quantity, addons)

    def view_cart(self,user_id):
        member = self.search_user_by_id(user_id)
        if not member:
            return "Error: User not found"
        cart = member.get_cart()
        cart_details = cart.get_cart_details()
        return cart_details

    def login(self):
        pass
    
    def register(self):
        pass

class User:
    def __init__(self,user_id, name, tel, password):
        self.__user_id = user_id
        self.__name = name
        self.__tel = tel
        self.__password = password

    def get_id(self):
        return self.__user_id 
    
    def logout(self):
        pass
    
    def update_profile(self):
        pass

class Member(User):
    def __init__(self, user_id,name, tel, password):
        super().__init__(user_id,name, tel, password)
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
        
    def add_to_cart(self, menu, quantity, addons=None):
        if quantity <= 0:
            return "Error: Quantity must be a positive number."
        
        total_price = menu.get_price() * quantity

        if isinstance(menu, Burger) and addons:
            for addon in addons:
                if addon in menu.get_addons():
                    total_price += menu.get_addons()[addon] * quantity  

        self.__cart.add_item(menu, quantity, total_price)
        
        return "Success"
    
    def place_order(self):
        pass
    
    def exchange_point_to_coupon(self):
        pass
    
    def view_order_history(self):
        pass
    
    def update_address(self):
        pass

class Admin(User):
    def __init__(self, user_id,name, tel, password,admin_type):
        super().__init__(user_id,name, tel, password)
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
        return self.__detail

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
    def __init__(self, category, menu_id, name, price, detail): 
        super().__init__(category, menu_id, name, price, detail)
        self.__addons = {}
    
    def add_addon(self, addon, price):
        self.__addons[addon] = price

    def get_addons(self):
        return self.__addons

    def calculate_total_price(self):
        return self.get_price() + sum(self.__addons.values())

    def __str__(self):
        addons_str = ", ".join([f"{addon} (+${price})" for addon, price in self.__addons.items()])
        return f"{self.get_name()} - ${self.get_price()} ({addons_str})" if addons_str else f"{self.get_name()} - ${self.get_price()}"

class Cart:
    def __init__(self):
        self.__item_list = []
    
    def add_item(self, menu, quantity, total_price):
        for item in self.__item_list:
            if item.get_menu().get_id() == menu.get_id():
                item.update_quantity(quantity, total_price)
                return "Item quantity updated in cart."
        
        new_item = CartItem(menu, quantity, total_price)
        self.__item_list.append(new_item)
        return "Item added to cart."

    def get_item_list(self):
        return self.__item_list
    
    def calculate_total_price(self):
        return sum(item.get_total_price() for item in self.get_item_list())

    def get_cart_details(self):
        if not self.get_item_list():
            return "Cart is empty"
            
        details = [str(item) for item in self.get_item_list()]
        details.append(f"Total Price: ${self.calculate_total_price():.2f}")
        return "\n".join(details)

    def __str__(self):
        return "\n".join(str(item) for item in self.__item_list) if self.__item_list else "Cart is empty"
    
    def remove_item(self, menu_id):
        self.__item_list = [item for item in self.__item_list if item.get_menu().get_id() != menu_id]

    def get_total(self):
        pass

class CartItem:
    def __init__(self, menu, amount,total_price):
        self.__menu = menu
        self.__amount = amount
        self.__total_price = total_price
        
    def get_menu(self):
        return self.__menu
    
    def add_cart_item(self,menu,amount):
        self.__menu = menu
        self.__amount = amount

    def get_quantity(self):
        return self.__amount

    def get_total_price(self):
        return self.__total_price

    def update_quantity(self, quantity, total_price):
        self.__amount += quantity
        self.__total_price += total_price
        
    def __str__(self):
        return f"{self.__menu.get_name()} x {self.__amount} - Total: ${self.__total_price:.2f}"

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
    admin = Admin(1,"Admin User", "123456789", "adminpass", "SuperAdmin")
    member = Member(2,"John Doe", "987654321", "memberpass")
    
    system._System__user_list = [admin, member]
    # Assign an address to the member
    address = Address("John's Home", "123 Street, City, Country")
    member.update_address = address

    member_id = member.get_id()
    
    # Create menu items
    burger = Burger("Fast Food", 1, "Cheese Burger", 5.99, "Delicious cheeseburger")
    drink = Beverage("Beverage", 2, "Coke", 1.99, "Refreshing drink", "Medium")
    snack = Snack("Snacks", 3, "French Fries", 2.99, "Crispy and golden")
    
    menu_set = MenuSet("Combo", 4, "Burger Combo", 9.99, "Burger with fries and drink")
    menu_set.add_menu_item = [burger, drink, snack]
    burger.add_addon("More_Patty",1)
    burger.add_addon("Bacon",0.75)
    burger.add_addon("More_Cheese",0.5)
    system._System__menu_list = [burger, drink, snack, menu_set]

    cart = member.get_cart()
    system.add_to_cart(member_id, burger, 2)
    system.add_to_cart(member_id, drink, 5)
    system.add_to_cart(member_id, snack, 2)
    system.add_to_cart(member_id, menu_set, 2)
   
    return system,member,member_id

system, member,member_id= create_mockup_instances()
cart_details = system.view_cart(member_id)
total_price = member.get_cart().calculate_total_price()

# print(cart_details)

@rt('/')
def get():
    return Container(
        Div(
            Div(
                Div(
                    Button("☰", 
                        style="""
                            background: transparent; 
                            border: none; 
                            color: #502314;
                            font-size: 24px;
                            width: 40px; 
                            height: 40px;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            margin: 0;
                            padding: 0;
                            cursor: pointer;
                        """
                    ),
                    Img(src="https://i.imgur.com/fCpADUO.png", 
                        style="width: 55px; height: auto; margin: 0px;"
                    ),
                    H2("Burger Kong", style="color: #502314; margin: 0;"),
                    style="display: flex; align-items: center; gap: 10px;"
                ),
                Div(
                    Button(
                        Img(src="https://i.imgur.com/Xyhfm0Q.png", style="width: 40px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;"),
                    Button(
                        Img(src="https://i.imgur.com/AcIDazc.png", style="width: 40px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;"),
                    Button(
                        Img(src="https://i.imgur.com/2eQjSEg.png", style="width: 40px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;"),
                        style="display: flex; align-items: center; gap: 5px; margin-left: 20px;" 
                    ),
                style="display: flex; justify-content: space-between; align-items: center; width: 100%;"
            ),
            style="""
                width: 100%; 
                background: #f5ebdc; 
                padding: 15px; 
                border-bottom: 2px solid #502314;
                position: fixed; 
                top: 0; 
                left: 0; 
                width: 100%; 
                z-index: 1000;
                box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.5);
            """
        ),
        Body(
            Div(
                H1("BurgerKong Cart", style="color: #502314; background: #f5ebdc; text-align: center; padding: 10px; padding-top: 70px;"),
                Div(
                    Div(
                        Div(
                            H2("Your Order", style="color: #502314;"),
                            Button("Add more", style="background: #502314; color: white; padding: 5px 10px; border: none; border-radius: 10px; text-align: center;"),
                            style="display: flex; justify-content: space-between; align-items: center; width: 100%; padding-bottom: 10px;"
                        ),
                        Div(id="cart-items",
                            *[Div(
                                Div(f"{item.get_menu().get_name()} x {item.get_quantity()} ", 
                                    style="font-size: 20px; font-weight: bold; color: #502314; padding: 5px;"),
                                Div(f"${item.get_total_price():.2f}", 
                                    style="font-size: 20px; font-weight: bold; color: #502314; padding: 5px;"),
                                style="display: flex; justify-content: space-between; width: 100%; border-bottom: 1px solid rgba(80, 35, 20, 0.2); padding: 5px 0;"
                            ) for item in member.get_cart().get_item_list()],
                            style="flex-grow: 1; width: 98%; align-items: flex-start; overflow-y: auto; padding: 10px;"
                        ),
                        Div(
                            H3("Discount:", style="color: #502314;"),
                            H2(f"Total: ${total_price:.2f}", id="total", style="color: #D00000; font-weight: bold; margin-top: 10px;"),  
                            Div(
                                Button("Checkout",style="font-size: 20px; font-weight: bold; background-color: #D00000; color: #ffffff; width: 50%; padding: 10px; border: none; display: block; margin: auto; border-radius: 10px;"),
                                style="width: 100%; display: flex; justify-content: center; margin-top: 15px;"
                            ),
                            style="display: flex; flex-direction: column; width: 100%; padding-top: 15px; margin-top: auto;"
                        ),
                        style="display: flex; flex-direction: column; width: 100%; height: 100%; flex-grow: 1;"
                    ),
                    style="display: flex; flex-direction: column; background: #f5ebdc; padding: 20px; border-radius: 30px; width: 75%; height: 90vh; margin: auto; border: 1px solid #502314;"
                ),
                 style="display: flex; flex-direction: column; align-items: center; gap: 20px; width: 100%;"
            ),
            style="background: #f5ebdc; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 20px;"
        )
)

@rt('/cart/add/{id}')
def post(id: int):
    product = next((p for p in system._System__menu_list if p.get_id() == id), None)
    if not product:
        return "Product not found"
    
    result = system.add_to_cart(member_id, product, 1, [])

    if result != "Success":
        return result
    
    cart_details = system.view_cart(member_id)
    
    return Div(
        cart_details 
    )

serve()
