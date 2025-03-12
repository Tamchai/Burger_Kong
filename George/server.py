# count = 1
current_user_id = None

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
    def get_name (self):
        return self.__name
    def get_tel (self):
        return self.__tel
    def get_password (self):
        return self.__password
    
    def __str__(self):
        return f"{self.__name} {self.__password}"

class Member(User):
    def __init__(self, user_id,name, tel, password,lastname):
        super().__init__(user_id,name, tel, password)
        self.__order_list = []
        self.__address = None
        self.__payment = None
        self.__point = 0
        self.__coupon_list = []
        self.__cart = Cart()
        self.__current_id = 1001
        self.__lastname = lastname

    def get_cart(self):
        return self.__cart
    def get_point(self):
        return self.__point
    def set_cart(self, cart):
        self.__cart = cart

    def get_order_list(self):
        return self.__order_list
    
    def add_to_cart(self, menu, quantity, addons=None,sizes=None):
        if quantity <= 0:
            return "Error: Quantity must be a positive number."

        # Check if the menu item supports add-ons (e.g., Burger) or not
        if (isinstance(menu, Burger) or isinstance(menu,MenuSet)) and addons:
            addons = tuple(sorted(addons))  # Sort to avoid treating different orderings as different
        else:
            addons = tuple()  # No add-ons for non-Burger items or when no addons provided

        total_price = menu.get_price() * quantity
        if isinstance(menu, Burger) and addons:
            for addon in addons:
                if addon in menu.get_addons():
                    total_price += menu.get_addons()[addon] * quantity
                    
        if isinstance(menu, Beverage):
            size_price = {
                "Small":1,
                "Medium":1.5,
                "Big":2
            }
            if sizes in size_price:
                total_price += (menu.get_price() * size_price[sizes]) 
            
            
        
        # Add the item to the cart, distinguishing by menu ID + add-ons
        if isinstance(menu, Burger) :
            self.__cart.add_item(menu, quantity, total_price, cart_addons=addons)
        elif isinstance(menu, Beverage):
            self.__cart.add_item(menu, quantity, total_price, cart_sizes=sizes)
        else:
            self.__cart.add_item(menu, quantity, total_price)
        return total_price



    def set_payment_method(self, payment_method):
        self.__payment = payment_method
    
    def checkout(self):
        """ดึงข้อมูลสรุปออเดอร์"""
        return self.__cart.get_cart_details()

    def create_order(self):
        if not self.__cart.get_item_list():
            return "Error: Cart is empty!"
        
        total_price = self.__cart.calculate_total_price()
        order = Order(self.__current_id, self, total_price, status="pending")
        
        self.__current_id += 1
        self.__order_list.append(order)
        self.__cart = Cart()  # clear cart
        return order  # Return the order object instead of order.get_id()
 # คืนค่า order_id เพื่อใช้ภายหลัง

    def pay_order(self, order_id, payment_method):
        """ชำระเงินสำหรับออเดอร์ที่เลือก"""
        for order in self.__order_list:
            if order.get_id() == order_id:
                if order.get_status() != "pending":
                    return f"Error: Order {order_id} is already processed."

                # ชำระเงิน
                payment_status = payment_method.process_payment(order.get_total_price())

                if "Successful" in payment_status:
                    order.set_status("paid")
                    self.__point += 10
                    return f"Order {order_id} has been successfully paid."
                else:
                    return f"Payment failed: {payment_status}"

        return "Error: Order not found."

    def add_coupon_to_list(self,coupon):
        self.__coupon_list.append(coupon)

    def get_coupon(self):
        return self.__coupon_list
    
    def remove_coupon(self, coupon):
        if coupon in self.__coupon_list:
            self.__coupon_list.remove(coupon)

    def exchange_point_to_coupon(self, coupon_code):
        # """แลกแต้มเป็นคูปองจากลิสต์ที่มีอยู่"""
        available_coupons = [coupon for coupon in system.get_coupon_list() if coupon.get_name() == coupon_code]

        if not available_coupons:
            return "Error: Coupon not found or invalid."

        selected_coupon = available_coupons[0]
        required_points = selected_coupon.get_discount() * 10  # Example: 10% discount requires 100 points

        if self.__point < required_points:
            return "Error: Not enough points."

        # Deduct points and add the coupon
        self.__point -= required_points
        self.__coupon_list.append(selected_coupon)

        return f"Successfully exchanged {required_points} points for {selected_coupon.get_code()} ({selected_coupon.get_discount()}% discount)!"
    
    def update_address(self, name, detail):
        """Update or set the member's address"""
        self.__address = Address(name, detail)
        return f"Address updated to: {name}, {detail}"

    def get_address(self):
        if self.__address:
            return f"{self.__address._Address__name}: {self.__address._Address__detail}"
        return "No address set."

    def view_order_history(self):
        if not self.__order_list:
            return "No past orders."
        return "\n".join(str(order) for order in self.__order_list)

class Admin(User):
    def __init__(self, user_id,name, tel, password,admin_type):
        super().__init__(user_id,name, tel, password)
        self.__type = admin_type
    
    def get_type(self):
        return self.__type
    
    def view_orders(self, system):
        all_orders = []
        for user in system.get_user_list():
            if isinstance(user, Member):  # Only members have orders
                all_orders.extend(user.get_order_list())
        return "\n".join(str(order) for order in all_orders) if all_orders else "No orders found."

    def manage_menu(self, system, action, menu_item=None, menu_id=None):
        if action == "add" and menu_item:
            return system.add_menu(menu_item)  # Let System handle menu addition

        elif action == "remove" and menu_id:
            return system.remove_menu(menu_id)  # Let System handle menu removal

        return "Invalid action or missing parameters."

class Menu:
    def __init__(self, category, menu_id, name, price, detail,src):
        self.__category = category
        self.__menu_id = menu_id
        self.__name = name
        self.__price = price
        self.__detail = detail
        self.__src = src
    
    def get_id(self):
        return self.__menu_id

    def get_details(self):
        return self.__detail

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price
    
    def get_category(self):
        return self.__category
    
    def get_src(self):
        return self.__src
    
class Snack(Menu):
    pass

class MenuSet(Menu):
    def __init__(self, category, menu_id, name, price, detail, src):
        super().__init__(category, menu_id, name, price, detail, src)
        self.__menu_set_list = []
    
    def add_menu_item(self,menu):
        self.__menu_set_list.append(menu)
    
    def remove_menu_item(self,menu):
        if menu in self.__menu_set_list:
            self.__menu_set_list.remove(menu)
    

class Beverage(Menu):
    def __init__(self, category, menu_id, name, price, detail, src):
        super().__init__(category, menu_id, name, price, detail, src)
        self.__size = None

    def set_size(self, size):
        self.__size = size
        
    def get_size(self):
        return self.__size
    
class Burger(Menu):
    def __init__(self, category, menu_id, name, price, detail,src):
        super().__init__(category, menu_id, name, price, detail,src)
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
        self.__applied_coupon = None
    
    # def add_item(self, menu, quantity, total_price, addons):
    #     for item in self.__item_list:
    #         if item.get_menu() == menu and item.get_menu().get_addons() == addons:
    #             item.update_quantity(quantity)
    #             return print("Item quantity updated in cart.")
        
    #     new_item = CartItem(menu, quantity, total_price, addons)
    #     self.__item_list.append(new_item)
    #     return "Item added to cart."
    def add_item(self, menu, quantity, total_price, cart_addons=None,cart_sizes=None):
        # Ensure addons are a tuple for consistent comparison
        cart_addons = tuple(sorted(cart_addons)) if cart_addons else tuple()  # Sort to handle ordering issues

        # Check if the same menu with the same add-ons already exists
        for item in self.__item_list:
            if item.get_menu() == menu and item.get_addons() == cart_addons:  # Correct access to __addons
                item.update_quantity(quantity)  # Update quantity if the same item with the same addons exists
                return "Item quantity updated in cart."
            elif item.get_menu() == menu and item.get_sizes() == cart_sizes:
                pass 
        # If no existing item matches, create a new item
        if isinstance(menu,Burger):
            new_item = CartItem(menu, quantity, total_price, cart_item_addons = cart_addons)
        elif isinstance(menu,Beverage):
            new_item = CartItem(menu, quantity, total_price, cart_item_sizes =  cart_sizes)
        else:
            new_item = CartItem(menu, quantity, total_price)
        self.__item_list.append(new_item)
        return "Item added to cart."

    def apply_coupon(self, coupon ,member):
        """ใช้คูปองลดราคา"""
        if coupon and isinstance(coupon, Coupon):
            self.__applied_coupon = coupon
            member.remove_coupon(coupon)
        else:
            self.__applied_coupon = None
    
    def get_item_list(self):
        return self.__item_list
    
    def calculate_total_price(self):
        total = sum(item.get_total_price() for item in self.__item_list)
        if self.__applied_coupon:
            discount_amount = (self.__applied_coupon.get_discount() / 100) * total
            total -= discount_amount
        return round(total, 2)  


    def get_cart_details(self):
        """ดึงข้อมูลสินค้าในตะกร้า พร้อมราคารวม"""
        details = [str(item) for item in self.__item_list]
        total_before = sum(item.get_total_price() for item in self.__item_list)
        total_after = self.calculate_total_price()

        details.append(f"Total Before Discount: ${total_before:.2f}")
        if self.__applied_coupon:
            details.append(f"Coupon Applied: {self.__applied_coupon.get_name()} (-{self.__applied_coupon.get_discount()}%)")
        details.append(f"Total After Discount: ${total_after:.2f}")

        return "\n".join(details)
    
    def __str__(self):
        return "\n".join(str(item) for item in self.__item_list) if self.__item_list else "Cart is empty"
    
    def remove_item(self, menu, addons=None, sizes=None):
        for item in self.__item_list:
            if isinstance(menu,Burger) or isinstance(menu,MenuSet):
                if item.get_menu().get_id() == menu.get_id() and item.get_menu().get_addons() == menu.get_addons():
                    self.__item_list.remove(item)
                    return "Success"
            elif isinstance(menu,Beverage):
                if item.get_menu().get_id() == menu.get_id() and item.get_menu().get_size() == menu.get_size():
                    self.__item_list.remove(item)
                    return "Success"
            else:
                if item.get_menu().get_id() == menu.get_id():
                    self.__item_list.remove(item)
                    return "Success"
        return "Item not found in cart."
        pass
    
    def checkout(self):
        pass
    
class CartItem:
    def __init__(self, menu, amount, total_price, cart_item_addons=None, cart_item_sizes=None):
        self.__menu = menu
        self.__amount = amount
        self.__total_price = total_price
        self.__addons = cart_item_addons  # Store add-ons to distinguish different combinations
        self.__sizes = cart_item_sizes

    def get_menu(self):
        return self.__menu

    def get_total_price(self):
        return self.__total_price
    def get_quantity(self):
        return self.__amount
    def get_addons(self):
        return self.__addons
    
    def get_sizes(self):
        return self.__sizes
    
    def __str__(self):
        addons_str = ", ".join(self.__addons) if self.__addons else "No addons"
        if isinstance(self.__menu,Burger) or isinstance(self.__menu,MenuSet):
            return f"{self.__menu.get_name()} x {self.__amount} - Add-ons: {addons_str} - Total: ${self.__total_price:.2f}"
        elif isinstance(self.__menu,Beverage):
            return f"{self.__menu.get_name()} x {self.__amount} - Size : {self.__sizes} - Total: ${self.__total_price:.2f}"
        else:
            return f"{self.__menu.get_name()} x {self.__amount} - Total: ${self.__total_price:.2f}"
        
    def update_quantity(self, quantity):
        """Updates the quantity of the cart item and recalculates total price."""
        self.__amount += quantity
        self.__total_price = self.__menu.get_price() * self.__amount
        if self.__addons:
            for addon in self.__addons:
                # Ensure the addon exists before updating the total price
                if addon in self.__menu.get_addons():
                    self.__total_price += self.__menu.get_addons()[addon] * self.__amount
                else:
                    print(f"Addon {addon} not found in the menu's addons.")



class Order:
    def __init__(self, order_id, member,total_price,status="Pending"):
        self.__order_id = order_id
        self.__status = status
        self.__member = member
        self.__total_price = total_price
        self.__cart_items = member.get_cart().get_item_list()  # ✅ Store cart items
        self.__payment = None

    def get_cart_items(self):
        return self.__cart_items
    
    def __str__(self):
        item_details = "\n".join(str(item) for item in self.__cart_items)
        return (
            # f"Order ID: {self.__order_id}\n"
            # f"Status: {self.__status}\n"
            # f"Total Price: ${self.__total_price:.2f}\n"
            f"Items:\n{item_details}\n"
        )
    def get_total_price(self):
        return self.__total_price

    def set_total_price(self, price):
        if price < 0:
            raise ValueError("Total price cannot be negative")
        self.__total_price = price
    def get_id(self):
        return self.__order_id

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def add_item(self):
        pass
    
    def remove_item(self):
        pass
    
    def calculate_total(self):
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
    
    def process_payment(self, amount):  
        """ดำเนินการชำระเงิน"""
        return f"Payment Successful via {self.__payment_method_name}"

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
    def __init__(self, name, discount, expire_date):
        self.__name = name
        self.__discount = discount
        self.__expire_date = expire_date
    def get_name(self):
        return self.__name
    def get_discount(self):
        return self.__discount
    def get_expire_date(self):
        return self.__expire_date

class System:
    
    def __init__(self):
        self.__user_list = []
        self.__menu_list = []
        self.__payment_method = PaymentMethod()
        self.__coupon_list = []
    
    def register(self, new_user):
        for user in self.__user_list:
            if user.get_name() == new_user.get_name():
                return False
        self.__user_list.append(new_user)
        # print(self.get_user_list())
        global current_user_id
        current_user_id = new_user.get_id()
        return True

    # def check_admin(self, username, password):
    #     for user in self.__user_list:
    #         if user.get_name() == username and user.get_password() == password:
    #             return user
    #     return False

    def get_coupon_list(self):
        return self.__coupon_list
    
    def add_coupon(self,coupon : Coupon):
        self.__coupon_list.append(coupon)
    def add_menu(self, menu_item : Menu):
        # """Adds a menu item to the system."""
        self.__menu_list.append(menu_item)
        return f"Menu item '{menu_item.get_name()}' added successfully."

    def remove_menu(self, menu_id):
        # """Removes a menu item from the system."""
        menu_to_remove = self.search_menu_by_id(menu_id)
        if menu_to_remove:
            self.__menu_list.remove(menu_to_remove)
            return f"Menu item '{menu_to_remove.get_name()}' removed successfully."
        return "Error: Menu item not found."

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
    
    def get_menu_list(self):
        return self.__menu_list  
    
    def add_user_list(self, user):
        self.__user_list.append(user)

    def display_menu(self):
        return [f"{menu_item.__class__.__name__}: {menu_item._Menu__name} - ${menu_item._Menu__price}" for menu_item in self.__menu_list]

    def get_user_list(self):
        return self.__user_list
    
    def check_password(self, input_username, input_passwd):
        global current_user_id
        for user in self.__user_list:
            if user.get_name() == input_username and user.get_password() == input_passwd :
                current_user_id = user.get_id()
                return (True, user)
        return False
            
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
            
    def watch_cart(self, user_id):
        member = self.search_user_by_id(user_id)
        return member.get_cart()        
    
    def remove_from_cart(self,user_id,menu,addon=None,size=None):
        member = self.search_user_by_id(user_id)
        cart = member.get_cart()
        if isinstance(menu,Burger):
            return cart.remove_item(menu,addons = addon)
        elif isinstance(menu,Beverage):
            return cart.remove_item(menu,sizes = size)
    
    def show_total_price(self,user_id):
        member = self.search_user_by_id(user_id)
        cart = member.get_cart()
        return cart.calculate_total_price()
    
    def checkout(self,user_id):
        member = self.search_user_by_id(user_id)
        return member.checkout()
    
    def show_user_coupon(self,user_id):
        member = self.search_user_by_id(user_id)
        return member.get_coupon()
    
    def apply_coupon(self,user_id,coupon):
        member = self.search_user_by_id(user_id)
        cart = member.get_cart()
        return cart.apply_coupon(coupon,member)
    
    def create_order(self,user_id):
        member = self.search_user_by_id(user_id)
        return member.create_order()
    
    def pay_order(self,user_id,order,payment_method):
        member = self.search_user_by_id(user_id)
        return member.pay_order(order,payment_method)
    
    def exchange_point_to_coupon(self,user_id,point):
        member = self.search_user_by_id(user_id)
        return member.exchange_point_to_coupon(point)
    
    def add_to_cart(self, user_id, menu_item, quantity, addon=None,size = None):
        member = self.search_user_by_id(user_id)
        if not menu_item:
            return "Error: Menu item not found."
        if quantity <= 0:
            return "Error: Quantity must be a positive number."
        
        if isinstance(menu_item, Beverage):
            print(f"system:{size}")
            return member.add_to_cart(menu_item,quantity, sizes =size)
        elif isinstance(menu_item, Burger):
            print(f"system:{addon}")
            return member.add_to_cart(menu_item, quantity, addons = addon)
        else:
            return member.add_to_cart(menu_item, quantity)

def create_mockup_instances():
    system = System()
    
    # Create admin and member users
    admin = Admin(1, "admin", "123456789", "admin", "SuperAdmin")
    member = Member(2, "aa", "987654321", "aa","Doe")
    
    system._System__user_list = [admin, member]
    
    # Assign an address to the member
    member.update_address("Home", "123 Main Street, City, Country")  # ✅ Proper method call
    member2 = Member(3, "ss", "987654321", "ss","Doe")
    system.add_user_list(member2)
    
    # Create menu items
    burger = Burger("Burger", 1, "Ultimate Bacon Burger", 7.59, "Delicious Bacon Burger",  "/picture/Burger/Ultimate-Bacon-Burger.png")
    burger2 = Burger("Burger", 2, "Mushroom Swiss Burger", 5.55, "Delicious Mushroom Swiss Burger",  "/picture/Burger/Mushroom-Swiss-Burger.png")
    burger3 = Burger("Burger", 3, "Grilled Beef Burger", 5.99, "Let's Try Grilled Beef Burger",  "/picture/Burger/Grilled-Beef-Burger.png")
    burger4 = Burger("Burger", 4, "Double Whopper", 5.99, "Delicious Double-Whopper",  "/picture/Burger/Double-Whopper.png")
    burger5 = Burger("Burger", 5, "Chicken Fingers Burger", 6.99, "Delicious Chicken Fingers Burger",  "/picture/Burger/chicken-fingers-burger.png")
    burger6 = Burger("Burger", 6, "Cheese Burger Chicken", 9.99, "Delicious Cheese Burger Chicken",  "/picture/Burger/Cheeseburger-chicken.png")
    burger7 = Burger("Burger", 7, "Burger ham and Cheese", 8.99, "Let's Try This Burger ham and Cheese",  "/picture/Burger/burger-ham-and-cheese.png")
    burger8 = Burger("Burger", 8, "Burger Double Cheese", 10.99, "Delicious Burger Double Cheese",  "/picture/Burger/burger-double-cheese.png")

    snack = Snack("Snack", 100, "Chicken pop", 2.99, "Do not eat French Fries", "/picture/Snack/chicken-pop.png")
    snack2 = Snack("Snack", 101, "Chocokate Lava Cake", 3.99, "Medium French Fries", "/picture/Snack/Chocokate-Lava-Cake.png")
    snack3 = Snack("Snack", 102, "French Fries XXL", 10.99, "Bucket French Fries", "/picture/Snack/french-fries.png")
    snack4 = Snack("Snack", 103, "Nuggets", 39.99, "Unlimited French Fries", "/picture/Snack/Nuggets.png")
    snack5 = Snack("Snack", 104, "Onion Ring", 39.99, "Unlimited French Fries", "/picture/Snack/Onion-Rings.png")
    snack6 = Snack("Snack", 105, "Whopper Poutune", 39.99, "Unlimited French Fries", "/picture/Snack/Whopper-Poutune.png")
    snack7 = Snack("Snack", 106, "French Fries Unlimited", 39.99, "Unlimited French Fries", "/picture/Snack/french-fries.png")

    drink = Beverage("Beverage", 200, "Water", 1.99, "Refreshing drink",  "/picture/Beverage/Bottled-Water.png")
    drink2 = Beverage("Beverage", 201, "Refill Coke", 3.99, "Refill COCACOLA",  "/picture/Beverage/cola.png")
    drink3 = Beverage("Beverage", 202, "Lemon Juice Lemonade", 1.99, "Refreshing drink",  "/picture/Beverage/Lemon-juice-Lemonade.png")
    drink4 = Beverage("Beverage", 203, "Orange Juice", 3.99, "Refill COCACOLA",  "/picture/Beverage/Orange-juice.png")
    drink5 = Beverage("Beverage", 204, "Coke", 1.99, "Refreshing drink",  "/picture/Beverage/cola.png")
    drink6 = Beverage("Beverage", 205, "Strawberry Juice", 3.99, "Refill COCACOLA", "/picture/Beverage/strawberry-juice.png")
    
    menu_set = MenuSet("Combo Set", 300, "Burger Combo", 9.99, "Burger with fries and drink", "/picture/Combo Set/Cheese Overload Set.png")
    menu_set2 = MenuSet("Combo Set", 301, "Burger Combo", 9.99, "Burger with fries and drink", "/picture/Combo Set/Chicken-Chicken-Cheese-Set.png")
    menu_set3 = MenuSet("Combo Set", 302, "Burger Combo", 9.99, "Burger with fries and drink", "/picture/Combo Set/Classic Whopper Meal.png")
    menu_set4 = MenuSet("Combo Set", 303, "Burger Combo", 9.99, "Burger with fries and drink", "/picture/Combo Set/Double Cheese Overload Set.png")
    menu_set5 = MenuSet("Combo Set", 304, "Burger Combo", 9.99, "Burger with fries and drink", "/picture/Combo Set/Mega Stack Bundle.png")
    menu_set6 = MenuSet("Combo Set", 305, "Burger Combo", 9.99, "Burger with fries and drink", "/picture/Combo Set/Whopper and Cheese Burger Set.png")

    coupon1 = Coupon("DISCOUNT40", 40, "2025-12-31")
    coupon2 = Coupon("DISCOUNT30", 30, "2025-12-31")
    coupon3 = Coupon("DISCOUNT20", 20, "2025-12-31")

    system.add_coupon(coupon1)
    system.add_coupon(coupon2)
    system.add_coupon(coupon3)
    
    menu_set.add_menu_item = [burger, drink, snack]
    member.add_coupon_to_list(Coupon("DISCOUNT10", 10, "2025-12-31"))
    for i in [burger, burger2, burger3, burger4,burger5, burger6, burger7, burger8,  snack, snack2, snack3, snack4, snack5, snack6, menu_set, menu_set2, menu_set3, menu_set4, menu_set5, menu_set6, drink, drink2, drink3, drink4, drink5, drink6]:
        system.add_menu(i) 
    for i in system.get_menu_list():
        if i.get_category() == "Burger":
            i.add_addon("More_Patty",1)
            i.add_addon("Bacon",0.75)
            i.add_addon("More_Cheese",0.5)
    cart = member.get_cart()
    
    return {
        "system": system,
        "admin": admin,
        "member": member,
        "menu_items": [burger, drink, snack],
        "menu_set": menu_set,
        "cart": cart,
    }


# Example usage with mockup data

mockup_data = create_mockup_instances()
system = mockup_data["system"]
member = mockup_data["member"]
admin = mockup_data["admin"]
def testrun(system, member,admin):
    print("Displaying menu:")
    print(system.display_menu())
    user_id = 2
    add_on = ["Bacon", "More_Patty"]
    print("\nSelecting and adding menu items to cart:")
    
    # เลือกเมนูเบอร์เกอร์
    selected_menu = system.select_menu(1)
    print(f"Selected menu: {selected_menu}")
    
    result = system.add_to_cart(user_id, selected_menu, 1, add_on)
    print(f"Add to cart result: {result}")



    selected_menu = system.select_menu(2)
    result = system.add_to_cart(user_id, selected_menu, 2, add_on)
    result = system.add_to_cart(user_id, selected_menu, 2, add_on)
    result = system.add_to_cart(user_id, selected_menu, 2, None)
    result = system.add_to_cart(user_id, selected_menu, 2, None)
    
    selected_menu = system.select_menu(200)
    result = system.add_to_cart(user_id, selected_menu, 2, size="Big")
    result = system.add_to_cart(user_id, selected_menu, 2, size="Small")
    # ดูรายละเอียดของตะกร้า
    print(system.checkout(user_id))
    print("\nCart contents before removing an item:")
    print(system.watch_cart(user_id))

    # ลบสินค้าออกจากตะกร้า
    selected_menu = system.select_menu(1)
    print("\nRemoving an item from cart (Burger)...")
    system.remove_from_cart(user_id,selected_menu)
    selected_menu = system.select_menu(2)
    system.remove_from_cart(user_id,selected_menu, addon=["Bacon", "More_Patty"])
    system.remove_from_cart(user_id,system.select_menu(200), size="Big")
    # ดูรายละเอียดตะกร้าหลังลบ
    print("\nCart contents after removing Burger:")
    print(system.watch_cart(user_id))

    # ตรวจสอบยอดรวมของตะกร้า
    total_price = system.show_total_price(user_id)
    print(f"\nTotal price after removing Burger: ${total_price:.2f}")


    print("\nCart Summary ก่อนใช้คูปอง:")
    
    print(system.checkout(user_id))

    # ใช้คูปองลดราคา 10%
    coupon = system.show_user_coupon(user_id)
    index = 0 #Index ของ Dropdown เด้อครับพี่น้อง
    print(coupon)
    system.apply_coupon(user_id,coupon[index])
    total_price = system.show_total_price(user_id)
    print(f"\nc ${total_price:.2f}")
   
    
    # แสดงตะกร้าหลังใช้คูปอง
    print("\nCart Summary หลังใช้คูปอง:")
    print(system.checkout(user_id))
    print(f"Total = {total_price}")
    
    
    print(coupon)

    # กดยืนยันออเดอร์
    print("\nCreating Order...")
    # payment = CreditCard("1234567890123456", "12/25", "123")
    order_id = system.create_order(user_id)

    print("\nOrder List:")
    for order in member.get_order_list():
        print(f"aaa{order.get_total_price()}")
        print(order)
    
    payment_method = CreditCard("1234567890123456", "12/25", "123")
    print(system.pay_order(user_id,order_id,payment_method))
    for order in member.get_order_list():
        print(order)
    # Show available coupons before exchanging
    available_coupons = system.get_coupon_list()
    print("Available Coupons for Exchange:")
    for coupon in available_coupons:
        print(f"{coupon.get_name()} - {coupon.get_discount()}% discount")

    # Choose a coupon to exchange (assuming we pick the first one)
    if available_coupons:
        selected_coupon_code = available_coupons[0].get_name()
        print(f"\nAttempting to exchange for coupon: {selected_coupon_code}")
        print(system.exchange_point_to_coupon(user_id, selected_coupon_code))
    else:
        print("\nNo available coupons for exchange.")
    selected_menu = system.select_menu(2)
    result = system.add_to_cart(3, selected_menu, 2, add_on)
    result = system.add_to_cart(3, selected_menu, 2, add_on)
    result = system.add_to_cart(3, selected_menu, 2, None)
    result = system.add_to_cart(3, selected_menu, 2, None)
    
    selected_menu = system.select_menu(200)
    result = system.add_to_cart(3, selected_menu, 2, size="Big")
    result = system.add_to_cart(3, selected_menu, 2, size="Small")  
    user_id = 3
    print(system.checkout(user_id))
    print(system.watch_cart(user_id))
    print(system.show_total_price(user_id))
    print(system.checkout(user_id))    
    print(system.create_order(user_id))
    print(system.pay_order(user_id,1001,payment_method))
    selected_menu = system.select_menu(2)
    result = system.add_to_cart(3, selected_menu, 2, add_on)
    result = system.add_to_cart(3, selected_menu, 2, add_on)
    result = system.add_to_cart(3, selected_menu, 2, None)
    result = system.add_to_cart(3, selected_menu, 2, None)
    
    selected_menu = system.select_menu(200)
    result = system.add_to_cart(3, selected_menu, 2, size="Big")
    result = system.add_to_cart(3, selected_menu, 2, size="Small")  
    user_id = 3
    print(system.checkout(user_id))
    print(system.watch_cart(user_id))
    print(system.show_total_price(user_id))
    print(system.checkout(user_id))    
    print(system.create_order(user_id))
    print(system.pay_order(user_id,1,payment_method))
    for i in member.get_order_list():
        print("-------------")
        print(i)
    
        
    print(member.get_address())  # Output: Home: 123 Main Street, City, Country  
    print(member.update_address("Home", "gg"))
    print(member.get_address())  # Output: Home: 123 Main Street, City, Country

    # View order history
    print(member.view_order_history())
    # print("\n=== Viewing Orders After Order Created ===")
    print(admin.view_orders(system))  # Expect: Order should be displayed

    # ====== TESTING MENU MANAGEMENT ======
    print("\n=== Adding a New Menu Item ===")
    new_burger = Burger("Burger", 999, "Super Spicy Burger", 8.99, "Extra spicy burger", "/picture/spicy-burger.png")
    print(admin.manage_menu(system, "add", menu_item=new_burger))  # Expect: Menu added

    print("\n=== Displaying Menu After Adding New Item ===")
    print(system.display_menu())  # Expect: "Super Spicy Burger" should be listed

    print("\n=== Removing a Menu Item ===")
    print(admin.manage_menu(system, "remove", menu_id=999))  # Expect: Menu removed

    print("\n=== Displaying Menu After Removing Item ===")
    print(system.display_menu())  # Expect: "Super Spicy Burger" should be gone
    
    print(f"\n{system.search_user_by_id(2).get_id()} Order List:")
    for order in system.search_user_by_id(2).get_order_list():
        print(f"aaa{order.get_total_price()}")
        print(order)

    print(f"\n{system.search_user_by_id(3).get_id()} Order List:")
    for order in system.search_user_by_id(3).get_order_list():
        print(f"aaa{order.get_total_price()}")
        print(order)
testrun(system, member,admin)
