from fasthtml.common import * 
app, rt = fast_app(live=True)

class System:
    def __init__(self):
        self.__user_list = []
        self.__menu_list = []
        self.__payment_method = PaymentMethod()

    def add_menu(self, menu_item):
        self.__menu_list.append(menu_item)

    def filter_category(self, target_category):
        results = []
        for menu in self.__menu_list:
            if str(menu.get_category()).lower() == str(target_category).lower():
                results.append(menu)
        return results

    def search_products_by_name(self, search: str):
        result = []
        for i in self.get_menu_list():
            if search.lower() in i.get_name().lower():
                result.append(i)
        return result

    def display_menu(self):
        return [f"{menu_item.__class__.__name__}: {menu_item._Menu__name} - ${menu_item._Menu__price}" for menu_item in self.__menu_list]

    def get_menu_list(self):
        return self.__menu_list  
    
    def select_menu(self, menu_id):
        menu = self.search_menu_by_id(menu_id)
        return menu
    
    def search_menu_by_id(self, menu_id):
        for menus in self.__menu_list:
            if menu_id == menus.get_id():
                return menus

    def search_user_by_id(self, user_id):
        for users in self.__user_list:
            if users.get_id() == user_id:
                return users
             
    def add_to_cart(self, user_id, menu_item, quantity):
        member = self.search_user_by_id(user_id)
        if not menu_item:
            return "Error: Menu item not found."
        if quantity <= 0:
            return "Error: Quantity must be a positive number."
        member.add_to_cart(menu_item, quantity)
        
    def login(self):
        pass
    
    def register(self):
        pass

class User:
    def __init__(self, user_id, name, tel, password):
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
    def __init__(self, user_id, name, tel, password):
        super().__init__(user_id, name, tel, password)
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
        pass
    
    def exchange_point_to_coupon(self):
        pass
    
    def view_order_history(self):
        pass
    
    def update_address(self):
        pass

class Admin(User):
    def __init__(self, user_id, name, tel, password, admin_type):
        super().__init__(user_id, name, tel, password)
        self.__type = admin_type
    
    def manage_menu(self):
        pass
    
    def view_orders(self):
        pass

class Menu:
    def __init__(self, category, menu_id, name, price, detail, src):
        self.__category = category
        self.__menu_id = menu_id
        self.__name = name
        self.__price = price
        self.__detail = detail
        self.__src = src
    
    def get_src(self):
        return self.__src

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

    def get_category(self):
        return self.__category

class Snack(Menu):
    pass

class MenuSet(Menu):
    def __init__(self, category, menu_id, name, price, detail, src):
        super().__init__(category, menu_id, name, price, detail, src)
        self.__menu_set_list = []
    
    def add_menu_item(self):
        pass
    
    def remove_menu_item(self):
        pass
    
    def get_total_price(self):
        pass

class Beverage(Menu):
    def __init__(self, category, menu_id, name, price, detail, size, src):
        super().__init__(category, menu_id, name, price, detail, src)
        self.__size = size
    
    def set_size(self, size):
        self.__size = size

class Burger(Menu):
    def __init__(self, category, menu_id, name, price, detail, addon, src):
        super().__init__(category, menu_id, name, price, detail, src)
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
    
    def add_cart_item(self, menu, amount):
        self.__menu = menu
        self.__amount = amount
    
    def __str__(self):
        return f"{self.__menu.get_name()} x {self.__amount} (${self.__menu.get_price()} each)"
    
    def get_quantity(self):
        return self.__amount

    def update_quantity(self, quantity):
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
    admin = Admin(1, "Admin User", "123456789", "adminpass", "SuperAdmin")
    member = Member(2, "John Doe", "987654321", "memberpass")
    
    system._System__user_list = [admin, member]
    
    # Assign an address to the member
    address = Address("John's Home", "123 Street, City, Country")
    member.update_address = address
    
    # Create menu items
    burger = Burger("Burger", 1, "Ultimate Bacon Burger", 7.59, "Delicious Bacon Burger", "Extra Cheese", "/picture/Ultimate-Bacon-Burger.png")
    burger2 = Burger("Burger", 2, "Mushroom Swiss Burger", 5.55, "Delicious Mushroom Swiss Burger", "Extra Cheese", "/picture/Mushroom-Swiss-Burger.png")
    burger3 = Burger("Burger", 3, "Grilled Beef Burger", 5.99, "Let's Try Grilled Beef Burger", "Extra Cheese", "/picture/Grilled-Beef-Burger.png")
    burger4 = Burger("Burger", 4, "Double Whopper", 5.99, "Delicious Double-Whopper", "Extra Cheese", "/picture/Double-Whopper.png")
    burger5 = Burger("Burger", 5, "Chicken Fingers Burger", 6.99, "Delicious Chicken Fingers Burger", "Extra Cheese", "/picture/chicken-fingers-burger.png")
    burger6 = Burger("Burger", 6, "Cheese Burger Chicken", 9.99, "Delicious Cheese Burger Chicken", "Extra Cheese", "/picture/Cheeseburger-chicken.png")
    burger7 = Burger("Burger", 7, "Burger ham and Cheese", 8.99, "Let's Try This Burger ham and Cheese", "Extra Cheese", "/picture/burger-ham-and-cheese.png")
    burger8 = Burger("Burger", 8, "Burger Double Cheese", 10.99, "Delicious Burger Double Cheese", "Extra Cheese", "/picture/burger-double-cheese.png")

    snack = Snack("Snack", 100, "French Fries M", 2.99, "Do not eat French Fries", "/picture/french-fries.png")
    snack2 = Snack("Snack", 101, "French Fries L", 3.99, "Medium French Fries", "/picture/french-fries.png")
    snack3 = Snack("Snack", 102, "French Fries XXL", 10.99, "Bucket French Fries", "/picture/french-fries.png")
    snack4 = Snack("Snack", 103, "French Fries Unlimited", 39.99, "Unlimited French Fries", "/picture/french-fries.png")
    snack5 = Snack("Snack", 103, "French Fries Unlimited", 39.99, "Unlimited French Fries", "/picture/french-fries.png")


    drink = Beverage("Beverage", 200, "Coke", 1.99, "Refreshing drink", "Medium", "/picture/cola.png")
    drink2 = Beverage("Beverage", 201, "Refill Coke", 3.99, "Refill COCACOLA", "Medium", "/picture/cola.png")
    drink3 = Beverage("Beverage", 202, "Coke", 1.99, "Refreshing drink", "Medium", "/picture/cola.png")
    drink4 = Beverage("Beverage", 203, "Refill Coke", 3.99, "Refill COCACOLA", "Medium", "/picture/cola.png")
    drink5 = Beverage("Beverage", 204, "Coke", 1.99, "Refreshing drink", "Medium", "/picture/cola.png")
    drink6 = Beverage("Beverage", 205, "Refill Coke", 3.99, "Refill COCACOLA", "Medium", "/picture/cola.png")
    
    menu_set = MenuSet("Combo Set", 300, "Burger Combo", 9.99, "Burger with fries and drink", "picture/combo2.png")
    menu_set2 = MenuSet("Combo Set", 301, "Burger Combo", 9.99, "Burger with fries and drink", "picture/combo2.png")
    menu_set3 = MenuSet("Combo Set", 302, "Burger Combo", 9.99, "Burger with fries and drink", "picture/combo2.png")
    menu_set4 = MenuSet("Combo Set", 303, "Burger Combo", 9.99, "Burger with fries and drink", "picture/combo2.png")
    menu_set5 = MenuSet("Combo Set", 304, "Burger Combo", 9.99, "Burger with fries and drink", "picture/combo2.png")
    menu_set6 = MenuSet("Combo Set", 305, "Burger Combo", 9.99, "Burger with fries and drink", "picture/combo2.png")
    
    menu_set.add_menu_item = [burger, drink, snack]
    
    for i in [burger, burger2, burger3, burger4,burger5, burger6, burger7, burger8,  snack, snack2, snack3, snack4, snack5, menu_set, menu_set2, menu_set3, menu_set4, menu_set5, menu_set6, drink, drink2, drink3, drink4, drink5, drink6]:
        system.add_menu(i) 

    cart = member.get_cart()
    
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
# def test_add_to_cart(system, member):
#     print("Displaying menu:")
#     print(system.display_menu())
#     member_id = 2
    
#     print("\nSelecting and adding menu items to cart:")
#     selected_menu = system.select_menu(1)
#     print(f"Selected menu: {selected_menu}")
#     result = system.add_to_cart(member_id, selected_menu, 2)
#     print(f"Add to cart result: {result}")
#     print("Cart contents:")
#     print(member.get_cart())
    
#     selected_menu = system.select_menu(2)
#     result = system.add_to_cart(member_id, selected_menu, 2)
#     print("\nUpdated cart contents:")
#     print(member.get_cart())

# Example usage with mockup data
mockup_data = create_mockup_instances()
# test_add_to_cart(mockup_data["system"], mockup_data["member"])
system = mockup_data["system"]
pic = "/logo.png"

def product_card(p): 
    menu_id = p.get_id()
    return Card(
        H3(p.get_name(), style="text-align: center; margin: 10px 0;"),
        Img(src=p.get_src(), alt="ภาพตัวอย่าง", style="width: 100px; height: 100px; display: block; margin: auto;"),
        P(f"${p.get_price()}", style="text-align: center; font-weight: bold;"),
        Form(
            Input(type="hidden", name = str(menu_id)),
            Button("SeeDetail", type="submit"),
            action=f"/detail/{p.get_id()}",
            method="get"
        ),
        style=(
            "min-width: 150px; "
            "max-width: 200px; "
            "height: 300px; "
            "padding: 10px; "
            "text-align: center; "
            "background: #fff; "
            "border-radius: 10px; "
            "box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); "
            "display: flex; "
            "flex-direction: column; "
            "justify-content: space-between;"
        )
    )

@app.get('/search')
def search(search: str):
    results = system.search_products_by_name(search)
    return Div(
        Grid(
            *[product_card(p) for p in results], 
            style="""
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 15px;
                justify-items: center;
                align-items: center;
                margin-top: 160px;
                padding: 20px;
                background-color: #f5ebdc;
            # """
        ),id="product-list"
    )

@app.get('/filter')
def filter(category: str):
    results = system.filter_category(category)
    if category == 'All Menu': 
        return Div(
                Grid(
                    *[product_card(p) for p in system.get_menu_list()],
                    style="""
                        display: grid;
                        grid-template-columns: repeat(4, 1fr);
                        gap: 15px;
                        justify-items: center;
                        align-items: center;
                        margin-top: 160px;
                        padding: 20px;
                        background-color: #f5ebdc;
                    """
                ),id="product-list")
    else :
        return Div(
            Grid(
                *[product_card(p) for p in results], 
                style="""
                    display: grid;
                    grid-template-columns: repeat(4, 1fr);
                    gap: 15px;
                    justify-items: center;
                    align-items: center;
                    margin-top: 160px;
                    padding: 20px;
                    background-color: #f5ebdc;
                # """
            ),id="product-list")


@app.get("/")
def home():
    return Title("Burger Kong"),Container(
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
                    Form(
                        Input(id="search", name="search", placeholder="Search products...",
                            style="""
                                background: #f8e3c2; 
                                border: 2px solid #502314; 
                                color: #502314; 
                                padding: 8px 12px; 
                                border-radius: 10px;
                                font-size: 16px;
                                outline: none;
                                height: 40px;
                                width: 250px;
                            """),
                        hx_get="/search",
                        target_id="results",
                        hx_trigger="keyup delay:500ms",
                        hx_preserve="true",
                        style="display: flex; align-items: center; justify-content: center; margin-top: 10px;"
                    ),
                    Div(
                        Img(src="https://i.imgur.com/Xyhfm0Q.png",
                            style="width: 40px; height: auto;"),
                        Img(src="https://i.imgur.com/AcIDazc.png",
                            style="width: 40px; height: auto;"),
                        Img(src="https://i.imgur.com/Kj7efMN.png",
                            style="width: 40px; height: auto;"),
                        Img(src="https://i.imgur.com/2eQjSEg.png",
                            style="width: 40px; height: auto;"),
                        style="display: flex; align-items: center; gap: 15px; margin-left: 20px;" 
                    ),
                    style="color: #502314; font-size: 20px; font-weight: bold; display: flex; justify-content: flex-end; align-items: center;"
                ),
                style="display: flex; align-items: center; justify-content: space-between; align-items: center; width: 100%; gap: 15px;" 
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
            Form(Div(
                *[Button(text, name="category", value=text, id=text, 
                style="font-size: 36px; margin: 0 20px; font-weight: bold; color: #502314; background: none; border: none; cursor: pointer;")
                for text in ["All Menu", "Combo Set", "Burger", "Beverage", "Snack"]]
,
                style="""
                    position: absolute;
                    left: 0;
                    right: 0;
                    padding: 20px; 
                    background: #f8e3c2; 
                    margin-top: 40px; 
                    width: 100%; 
                    align-items: center;
                    display: flex;
                    justify-content: center;
                    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.5);
                """
            ),
                        hx_get="/filter",
                        target_id="results",
                        hx_trigger="click"),
            Div(
                Grid(
                    Div(*[product_card(p) for p in system.get_menu_list()],
                    style="""
                        display: grid;
                        grid-template-columns: repeat(4, 1fr);
                        gap: 15px;
                        justify-items: center;
                        align-items: center;
                        margin-top: 160px;
                        padding: 20px;
                        background-color: #f5ebdc;
                    """),
                ),
            id="results"),
            style="background: #f5ebdc; min-height: 100vh; display: flex; align-items: center; justify-content: center;"
        )
    )
@app.get("/detail/{menu_id}")
def detail(menu_id: int): 
    menu = system.select_menu(menu_id)
    if not menu:
        return "Menu item not found."
    return Title(f"{menu.get_name()} Detail"), Div(
        Div(
            Img(src=menu.get_src(), alt="Menu image", style="width: 100%; max-width: 300px; border-radius: 15px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);"),
            Div(
                H1(B(menu.get_name()), style="font-size: 32px; color: #502314;"),
                H3(f"Price: ${menu.get_price()}", style="font-size: 24px; color: #8b4513;"),
                P(menu.get_details(), style="font-size: 18px; color: #333; line-height: 1.5;"),
                Button("Add to Cart", style="background: #8b4513; color: white; padding: 10px 20px; font-size: 18px; border: none; border-radius: 10px; cursor: pointer; margin-top: 15px;"),
                style="text-align: left; max-width: 400px;"
            ),
            style="""
                display: flex;
                flex-direction: row;
                align-items: center;
                gap: 40px;
                max-width: 800px;
                width: 90%;
                background: white;
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.15);
            """
        ),
        style="""
            min-height: 100vh;
            width: 100vw;
            background-color: #f8e3c2;
            display: flex;
            align-items: center;
            justify-content: center;
        """
    )


serve()