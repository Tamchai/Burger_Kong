from fasthtml.common import *
app, rt = fast_app(live=true)
count = 1
class System:
    
    def __init__(self):
        self.__user_list = []
        self.__menu_list = []
        self.__payment_method = PaymentMethod()
    
    def display_menu(self):
        return [f"{menu_item.__class__.__name__}: {menu_item._Menu__name} - ${menu_item._Menu__price}" for menu_item in self.__menu_list]

    # def select_menu(self,menu_id):
    #     for menus in self.__menu_list:
    #         if menu_id == menus.get_id():
    #             return menus.get_details()
            
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

        # Ensure addons is a list if provided
        if isinstance(addons, str):  
            addons = [addons]  # Convert single string add-on to list
        elif addons is None or not isinstance(addons, (list, tuple)):  
            addons = []  # Ensure addons is always a list

        # If the item is a burger, calculate add-ons
        if isinstance(menu_item, Burger) and addons:
            for addon in addons:
                if addon in menu_item.get_addons():
                    total_price += menu_item.get_addons()[addon] * quantity  # Apply to each item

        # Pass the correct parameters
        return member.add_to_cart(menu_item, quantity, addons)


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

        # If the item is a burger, calculate add-ons
        if isinstance(menu, Burger) and addons:
            for addon in addons:
                if addon in menu.get_addons():
                    total_price += menu.get_addons()[addon] * quantity  # Apply to each item

        # Create cart item with updated price
        self.__cart.add_item(menu, quantity, total_price)
        
        return total_price

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
        self.__addons = {}  # Dictionary to store add-ons and their extra cost
    
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
    
    def add_item(self, menu, quantity,total_price):
        for item in self.__item_list:
            if item.get_menu() == menu:
                item.update_quantity(quantity)
                return "Item quantity updated in cart."
        new_item = CartItem(menu, quantity,total_price)
        self.__item_list.append(new_item)
        return "Item added to cart."

    
    def get_item_list(self):
        return self.__item_list
    
    def __str__(self):
        return "\n".join(str(item) for item in self.__item_list) if self.__item_list else "Cart is empty"
    
    def remove_item(self):
        pass
    
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
    
    def __str__(self):
     return f"{self.__menu.get_name()} x {self.__amount} - Total: ${self.__total_price:.2f}"

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
    admin = Admin(1,"Admin User", "123456789", "adminpass", "SuperAdmin")
    member = Member(2,"John Doe", "987654321", "memberpass")
    
    system._System__user_list = [admin, member]
    
    # Assign an address to the member
    address = Address("John's Home", "123 Street, City, Country")
    member.update_address = address
    
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
   
    # Create order linked to the member
    # order = Order(1001, member)
    # order.add_item = [cart_item1, cart_item2, cart_item3]
    # order.calculate_total = 15.96

    # qr_payment = QRCode("QR_DATA_12345")
    # credit_payment = CreditCard("1234567890123456", "12/25", "123")

    # payment = Payment(5001, "2025-02-13", order.calculate_total, "Completed", 2.0, qr_payment)

    # coupon = Coupon("SAVE10", 10, "2025-12-31")
    # member.exchange_point_to_coupon = [coupon]
    
    return system,member
system,member = create_mockup_instances()
# def test_add_to_cart(system, member):
#     print("Displaying menu:")
#     print(system.display_menu())
#     member_id = 2

#     print("\nSelecting and adding menu items to cart:")

#     selected_menu = system.select_menu(1)  # Select burger
#     print(f"Selected menu: {selected_menu}")

#     # Add burger with add-ons
#     result = system.add_to_cart(member_id, selected_menu, 2, ["Bacon","More_Patty"])
#     print(f"Add to cart result: {result}")
#     print("Cart contents:")
#     print(member.get_cart())

#     selected_menu = system.select_menu(2)  # Select beverage
#     result = system.add_to_cart(member_id, selected_menu, 2, " ")

#     print("\nUpdated cart contents:")
#     print(member.get_cart())
 
# test_add_to_cart(system,member)
selected_menu = system.select_menu(1)
member_id = member.get_id()
@rt('/')
def get():
    return Container(
        Div(
            Div(
                Div(
                    Button(
                        Img(src="https://i.imgur.com/fCpADUO.png", style="width: 50px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;"),
                    H2("Burger Kong", style="color: #502314; margin: 0;"),
                    style="display: flex; align-items: center; gap: 10px;"
                ),
                Div(
                    Button(
                        Img(src="https://i.imgur.com/Xyhfm0Q.png", style="width: 40px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;"),
                    Button(
                        Img(src="https://i.imgur.com/JZR6dA6.png", style="width: 45px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;"),
                    Button(
                        Img(src="https://i.imgur.com/2eQjSEg.png", style="width: 45px; height: auto;"),
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
                Div(
                    Div(
                        Img(
                            src="https://raw.githubusercontent.com/hdpngworld/HPW/main/uploads/6528f6e19c3d5-McDonald%20Double%20Cheeseburger%20hd%20png.png",
                            height="500px",
                            width="500px",
                            style="border-radius: 10px; padding: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);"
                        ),
                        Div(
                            H1(selected_menu.get_name(), style="color: #502314; font-size: 28px; font-weight: bold;"),
                            Hr(style="border: 1px solid #502314; opacity: 0.5; width: 100%;"),
                               P(selected_menu.get_details(), style="color: #502314; font-size: 18px;"),
                            style="margin-top: 20px; width: 100%; display: flex; flex-direction: column; align-items: left;"
                        ),
                        style="width: 50%; display: flex; flex-direction: column; align-items: left; padding: 20px;"
                    ),
                    Div(
                        H4("Add on", Class="section-title", style="color: #502314; font-size: 24px; font-weight: bold; "),                            
                        Form(
                            Div(
                                Label(CheckboxX(id="More_Patty", name="More_Patty", value="More_Patty", hx_post="/update_price", hx_target="#price", hx_trigger="change" , hx_swap="innerHTML" ),"More Patty +1$" , style="color: #502314; font-size: 18px; font-weight: bold;"),
                                Label(CheckboxX(id="Bacon", name="Bacon", value="Bacon",hx_post="/update_price", hx_target="#price", hx_trigger="change" , hx_swap="innerHTML"),"Bacon +0.75$" ,  style="color: #502314; font-size: 18px; font-weight: bold;"),
                                Label(CheckboxX(id="More_Cheese", name="More_Cheese", value="More_Cheese", hx_post="/update_price",hx_trigger="change" , hx_target="#price", hx_swap="innerHTML"), "More Cheese +0.5$", style="color: #502314; font-size: 18px; font-weight: bold;")
                            ),
                            Hr(style="border: 1px solid #000; opacity: 0.5;"),
                            Div(
                                Span("Quantity", Class="section-title", style="color: #502314; font-size: 22px; font-weight: bold;"),
                                Div(
                                    Button("-", hx_post="/decrement", hx_target="#count-container", hx_swap="innerHTML", Class="PMBtn",
                                            style="""
                                                background: transparent; 
                                                border: none; 
                                                color: #502314;
                                                font-size: 28px;
                                                width: 40px; 
                                                height: 40px;
                                                display: flex;
                                                align-items: center;
                                                justify-content: center;
                                                margin: 0;
                                                padding: 0;
                                                cursor: pointer;
                                                font-family: 'Arial', sans-serif !important;
                                            """),
                                    Div(
                                        Span(f"{count}", id="count", Class="PMNumber", style="margin: 0 1px; font-size: 22px; font-weight: bold; font-family: inherit;"),
                                        Input(type="hidden" ,name="count" ,id="count-input", value=f"{count}"),
                                        id="count-container"
                                    ),
                                    Button("+", hx_post="/increment", hx_target="#count-container", hx_swap="innerHTML" ,Class="PMBtn",
                                        style="""
                                                all: unset;
                                                background: transparent; 
                                                border: none; 
                                                color: #502314;
                                                font-size: 28px;
                                                width: 40px; 
                                                height: 40px;
                                                display: flex;
                                                align-items: center;
                                                justify-content: center;
                                                margin: 0;
                                                padding: 0;
                                                cursor: pointer;
                                                font-family: 'Arial', sans-serif !important;
                                            """),
                                    style="color: #502314; display: flex; align-items: center; gap: 10px;"
                                ),
                                Class="plusminus",
                                style="display: flex; align-items: center; justify-content: space-between; width: 100%;"
                            ),
                            H3(f"Price - {base_price:.2f}$", id="price", style="color: #D00; margin: 10px 0px 5px 0px; text-align: center;"),
                            Button("Add to Cart", type="submit", Class="add-to-cart-btn",
                                   style="""
                                        font-weight: bold; 
                                        font-size: 20px; 
                                        background-color: #D00; 
                                        border: 1px solid #502314; 
                                        border-radius: 20px; 
                                        margin: 5px auto 0 auto;
                                    """),
                            method="post",
                            action="/save",
                            style="margin-bottom: 0px; padding-bottom: 0px; display: flex; flex-direction: column;"
                        ),
                        style="""
                            width: 50%;
                            background: white;
                            padding: 10px 15px;
                            margin-top: 20px;
                            border-radius: 10px;
                            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
                            text-align: left;
                            height: 100%;
                            display: flex;
                            flex-direction: column;
                            gap: 8px;
                        """
                     ),
                    style="display: flex; justify-content: space-between; width: 90%; max-width: 1200px; margin: auto;"
                ),
                 style="display: flex; justify-content: space-between; align-items: flex-start; width: 90%; max-width: 1200px; margin: auto;"
            ),
            style="background: #f5ebdc; min-height: 100vh; display: flex; align-items: center; justify-content: center; margin-top: 5%; position: relative; "
        )
    )

base_price = selected_menu.get_price()
@rt('/save', methods=['POST'])
def post(More_Patty:str,Bacon:str,More_Cheese:str,count:int):
    return system.add_to_cart(member_id,selected_menu,count,[More_Patty,Bacon,More_Cheese])

@app.post("/increment")
def increment():
    global count
    count += 1
    return update_count_and_price()

@app.post("/decrement")
def decrement():
    global count
    count = max(1, count - 1)
    return update_count_and_price()

def update_count_and_price():
    return f"""
        <span id="count" style="font-size: 22px; font-weight: bold; font-family: inherit;">{count}</span>
        <input type="hidden" name="count" id="count-input" value="{count}">
        <div hx-post="/update_price" hx-trigger="load" hx-target="#price" hx-swap="innerHTML"></div>
    """

@app.post("/update_price")
async def update_price(
    More_Patty: Optional[str] = Form(None),
    Bacon: Optional[str] = Form(None),
    More_Cheese: Optional[str] = Form(None),
    count: int = Form(1)
):
    total_price = base_price * count  

    if More_Patty:
        total_price += 1.0 * count
    if Bacon:
        total_price += 0.75 * count
    if More_Cheese:
        total_price += 0.5 * count

    return f"Price - {total_price:.2f}$"






# @rt('/change')
# def get(): return P('Nice to be here!')

serve()
