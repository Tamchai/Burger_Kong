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
    
    def update_cart_items(self):
        cart_items = self.get_item_list()
        items_html = [
            Div(
                P(f"{item.get_menu().name} x {item.get_quantity()} - ${item.get_total_price():.2f}",
                style="font-size: 20px; color: #502314; font-weight: bold;"),
                Button("Remove", hx_post=f"/cart/remove/{item.get_menu().id}", hx_target="#cart-items", hx_swap="innerHTML",
                    style="background: #D00000; color: white; padding: 5px 10px; border: none; border-radius: 10px; text-align:center;"),
                style="display: flex; justify-content: space-between; align-items: center; padding: 5px;"
            )
            for item in cart_items
        ]
        return Div(*items_html, id="cart-items")


    def update_total(self):
        return H2(f"Total: ${self.calculate_total_price():.2f}", id="total", 
                style="color: #D00000; font-weight: bold; margin-top: 10px;",
              hx_swap_oob="true")

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

class Addres:
    def __init__(self, name, detail):
        self.__name = name
        self.__detail = detail
    
    def update_address(self):
        pass

class PaymentMethod:
    def __init__(self, payment_method_id=None, payment_method_name=None):
        self.__payment_method_id = payment_method_id
        self.__payment_method_name = payment_method_name
    
    def process_payment(self):
        pass

@dataclass
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def get_id(self):
        return self.id

products = [
    Product(1, "Cheese Burger", 5.99), 
    Product(2, "Coke", 1.99), 
    Product(3, "French Fries", 2.99),
    Product(4, "Burger Combo", 9.99)
]

cart = Cart()

def product_card(p):
    return Card(
        Div(
            H3(p.name, style="color: #502314; font-size: 22px; font-weight: bold; text-align: center;"),
            P(f"${p.price:.2f}", style="color: #D00000; font-size: 18px; text-align: center; font-weight: bold;"),
            Button(
                "Add to Cart", 
                hx_post=f"/cart/add/{p.id}", 
                hx_target="#cart-items",  
                hx_swap="innerHTML",
                style="background: #502314; color: white; padding: 10px 15px; border: none; border-radius: 15px; display: block; width: 100%; font-size: 16px; font-weight: bold;"
            ),
            style="padding: 15px; display: flex; flex-direction: column; align-items: center;"
        ),
        style="background: #f5ebdc; border-radius: 20px; padding: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); text-align: center; width: 200px;"
    )

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
                    Img(src="https://drive.google.com/uc?export=view&id=1oFUpKF61JStRktpR705JfVOzyjhlFRsS", 
                        style="width: 30px; height: auto; margin: 0 10px;"
                    ),
                    H2("Burger Kong", style="color: #502314; margin: 0;"),
                    style="display: flex; align-items: center; gap: 10px;"
                ),
                Div(
                    "user.png | notification.png | search.png | cart.png",
                    style="color: #502314; font-size: 20px; font-weight: bold; display: flex; justify-content: flex-end; align-items: center;"
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
        H1("BurgerKong Cart", style="color: #502314; background: #f5ebdc; text-align: center; padding: 10px; padding-top: 70px;"),
        Div(
            #ใช้แค่ส่ง ไม่ได้เอาไปใช้จริง
            Div(      
                *[product_card(p) for p in products], 
                id="product-list",
                style="width: 30%; padding: 15px; display: flex; flex-direction: column; gap: 15px;"
            ),
            Div(
                Div(
                    Div(
                        H2("Your Order", style="color: #502314;"),
                        Button("Add more", style="background: #502314; color: white; padding: 5px 10px; border: none; border-radius: 10px; text-align: center;"),
                        style="display: flex; justify-content: space-between; align-items: center; width: 100%; padding-bottom: 10px;"
                    ),
                    Div(id="cart-items", children=[],
                        style="flex-grow: 1; width: 100%;"
                    ),
                    Div(
                        H3("Discount:", style="color: #502314;"),
                        H2("Total: $0.00", id="total", style="color: #D00000; font-weight: bold; margin-top: 10px;"),  
                        Div(
                            Button("Checkout", 
                                style="font-size: 20px; font-weight: bold; background-color: #D00000; color: #ffffff; width: 50%; padding: 10px; border: none; display: block; margin: auto; border-radius: 10px;"),
                            style="width: 100%; display: flex; justify-content: center; margin-top: 15px;"
                        ),
                        style="display: flex; flex-direction: column; width: 100%; padding-top: 15px; margin-top: auto;"
                    ),
                    style="display: flex; flex-direction: column; width: 100%; height: 100%; flex-grow: 1;"
                ),
                style="display: flex; flex-direction: column; background: #f5ebdc; padding: 20px; border-radius: 30px; width: 75%; height: 90vh; margin: auto; border: 1px solid #502314;"
            ),
            style="display: flex; flex-direction: row; justify-content: center; align-items: flex-start; gap: 20px; width: 80%;"
        ),

        style="background: #f5ebdc; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 20px;"
    )
)

@rt('/cart/add/{id}')
def post(id: int):
    product = next((p for p in products if p.id == id), None)
    if not product:
        return "Product not found"

    cart.add_item(product, 1, product.price)

    return Div(
        cart.update_cart_items(),
        cart.update_total() 
    )

@rt('/cart/remove/{id}')
def remove_from_cart(id: int):
    product = next((p for p in products if p.id == id), None)
    if not product:
        return "Product not found"

    cart.remove_item(id)

    return Div(
        cart.update_cart_items(),
        cart.update_total()
    )
 
serve()
