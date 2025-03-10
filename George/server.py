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
    
    def add_to_cart(self, menu, quantity, addons=None):
        if quantity <= 0:
            return "Error: Quantity must be a positive number."
        
        total_price = menu.get_price() * quantity

        if isinstance(menu, Burger) and addons:
            for addon in addons:
                if addon in menu.get_addons():
                    total_price += menu.get_addons()[addon] * quantity  

        self.__cart.add_item(menu, quantity, total_price)
        
        return total_price

    def set_payment_method(self, payment_method):
        self.__payment = payment_method
    
    def checkout(self):
        """ดึงข้อมูลสรุปออเดอร์"""
        return self.__cart.get_cart_details()

    def create_order(self):
        """สร้างออเดอร์ที่รอจ่าย"""
        if not self.__cart.get_item_list():
            return "Error: Cart is empty!"
        
        total_price = self.__cart.calculate_total_price()
        
        # สร้างออเดอร์ใหม่ ที่สถานะเป็น "รอจ่าย"
        order = Order(self.__current_id, self, total_price, status="pending")

        
        self.__current_id += 1
        self.__order_list.append(order)  # บันทึกออเดอร์ในระบบ
        self.__cart = Cart()  # เคลียร์ตะกร้า
        
        return order.get_id()  # คืนค่า order_id เพื่อใช้ภายหลัง

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

    def exchange_point_to_coupon(self, point):
        """แลกแต้มเป็นคูปอง"""
        if self.__point < point:
            return "Error: Not enough points."

        discount = point // 10  # กำหนดส่วนลดของคูปอง (เช่น 10 แต้ม = 10% ส่วนลด)
        new_coupon = Coupon(f"POINT{point}", discount, "2025-12-31")  
        self.__coupon_list.append(new_coupon)
        self.__point -= point  

        return f"Successfully exchanged {point} points for a {discount}% discount coupon!"
    
    def view_order_history(self):
        pass
    
    def update_address(self):
        pass

class Admin(User):
    def __init__(self, user_id,name, tel, password,admin_type):
        super().__init__(user_id,name, tel, password)
        self.__type = admin_type
    
    def get_type(self):
        return self.__type
    
    def view_orders(self, system):
        """Fetches and displays all orders using System's method."""
        all_orders = []
        for user in system.get_user_list():
            if isinstance(user, Member):  # Only members have orders
                all_orders.extend(user.get_order_list())
        return "\n".join(str(order) for order in all_orders) if all_orders else "No orders found."

    def manage_menu(self, system, action, menu_item=None, menu_id=None):
        """Encapsulated approach to modify the menu via System."""
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
    
    def add_item(self, menu, quantity,total_price):
        for item in self.__item_list:
            if item.get_menu() == menu:
                item.update_quantity(quantity)
                return "Item quantity updated in cart."
        new_item = CartItem(menu, quantity,total_price)
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
            details.append(f"Coupon Applied: {self.__applied_coupon.get_code()} (-{self.__applied_coupon.get_discount()}%)")
        details.append(f"Total After Discount: ${total_after:.2f}")

        return "\n".join(details)
    
    def __str__(self):
        return "\n".join(str(item) for item in self.__item_list) if self.__item_list else "Cart is empty"
    
    def remove_item(self, menu):
        self.__item_list = [item for item in self.__item_list if item.get_menu().get_id() != menu.get_id()]
        # self.__item_list = self.__item_list.remove(menu_id)
    
    def checkout(self):
        pass
    
class CartItem:
    def __init__(self, menu, amount,total_price):
        self.__menu = menu
        self.__amount = amount
        self.__total_price = total_price
    def get_menu(self):
        return self.__menu
    def get_total_price(self):
        return self.__total_price
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
    def __init__(self, order_id, member,total_price,status="Pending"):
        self.__order_id = order_id
        self.__status = status
        self.__member = member
        self.__total_price = total_price
        self.__cart_items = member.get_cart().get_item_list()  # ✅ Store cart items
        self.__payment = None

    def __str__(self):
        item_details = "\n".join(str(item) for item in self.__cart_items)
        return (
            f"Order ID: {self.__order_id}\n"
            f"Status: {self.__status}\n"
            f"Total Price: ${self.__total_price:.2f}\n"
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
    def __init__(self, code, discount, expire_date):
        self.__code = code
        self.__discount = discount
        self.__expire_date = expire_date
    def get_code(self):
        return self.__code
    def get_discount(self):
        return self.__discount

class System:
    def add_menu(self, menu_item : Menu):
        # """Adds a menu item to the system."""
        self.menu_list.append(menu_item)
        return f"Menu item '{menu_item.get_name()}' added successfully."

    def remove_menu(self, menu_id):
        # """Removes a menu item from the system."""
        menu_to_remove = self.search_menu_by_id(menu_id)
        if menu_to_remove:
            self.menu_list.remove(menu_to_remove)
            return f"Menu item '{menu_to_remove.get_name()}' removed successfully."
        return "Error: Menu item not found."
    
    def __init__(self):
        self.__user_list = []
        self.__menu_list = []
        self.__payment_method = PaymentMethod()
    
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
    
    def remove_from_cart(self,user_id,menu_id):
        member = self.search_user_by_id(user_id)
        cart = member.get_cart()
        return cart.remove_item(menu_id)
    
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
    
    def add_to_cart(self, user_id, menu_id, quantity, addons=None):
        member = self.search_user_by_id(user_id)
        menu_item = self.search_menu_by_id(menu_id)
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

def create_mockup_instances():
    system = System()
    
    # Create admin and member users
    admin = Admin(1, "admin", "123456789", "admin", "SuperAdmin")
    member = Member(2, "aa", "987654321", "aa","Doe")
    
    system._System__user_list = [admin, member]
    
    # Assign an address to the member
    address = Address("John's Home", "123 Street, City, Country")
    member.update_address = address
    
    # Create menu items
    burger = Burger("Burger", 1, "Ultimate Bacon Burger", 7.59, "Delicious Bacon Burger",  "/picture/Ultimate-Bacon-Burger.png")
    burger2 = Burger("Burger", 2, "Mushroom Swiss Burger", 5.55, "Delicious Mushroom Swiss Burger",  "/picture/Mushroom-Swiss-Burger.png")
    burger3 = Burger("Burger", 3, "Grilled Beef Burger", 5.99, "Let's Try Grilled Beef Burger",  "/picture/Grilled-Beef-Burger.png")
    burger4 = Burger("Burger", 4, "Double Whopper", 5.99, "Delicious Double-Whopper",  "/picture/Double-Whopper.png")
    burger5 = Burger("Burger", 5, "Chicken Fingers Burger", 6.99, "Delicious Chicken Fingers Burger",  "/picture/chicken-fingers-burger.png")
    burger6 = Burger("Burger", 6, "Cheese Burger Chicken", 9.99, "Delicious Cheese Burger Chicken",  "/picture/Cheeseburger-chicken.png")
    burger7 = Burger("Burger", 7, "Burger ham and Cheese", 8.99, "Let's Try This Burger ham and Cheese",  "/picture/burger-ham-and-cheese.png")
    burger8 = Burger("Burger", 8, "Burger Double Cheese", 10.99, "Delicious Burger Double Cheese",  "/picture/burger-double-cheese.png")

    
    
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
    
    menu_set = MenuSet("Combo Set", 300, "Burger Combo", 9.99, "Burger with fries and drink", "/picture/combo2.png")
    menu_set2 = MenuSet("Combo Set", 301, "Burger Combo", 9.99, "Burger with fries and drink", "/picture/combo2.png")
    menu_set3 = MenuSet("Combo Set", 302, "Burger Combo", 9.99, "Burger with fries and drink", "/picture/combo2.png")
    menu_set4 = MenuSet("Combo Set", 303, "Burger Combo", 9.99, "Burger with fries and drink", "/picture/combo2.png")
    menu_set5 = MenuSet("Combo Set", 304, "Burger Combo", 9.99, "Burger with fries and drink", "/picture/combo2.png")
    menu_set6 = MenuSet("Combo Set", 305, "Burger Combo", 9.99, "Burger with fries and drink", "/picture/combo2.png")
    
    menu_set.add_menu_item = [burger, drink, snack]
    member.add_coupon_to_list(Coupon("DISCOUNT10", 10, "2025-12-31"))
    for i in [burger, burger2, burger3, burger4,burger5, burger6, burger7, burger8,  snack, snack2, snack3, snack4, snack5, menu_set, menu_set2, menu_set3, menu_set4, menu_set5, menu_set6, drink, drink2, drink3, drink4, drink5, drink6]:
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
        "address": address,
        "menu_items": [burger, drink, snack],
        "menu_set": menu_set,
        "cart": cart,
    }

mockup_data = create_mockup_instances()
system = mockup_data["system"]
member = mockup_data["member"]
def testrun(system, member):
    print("Displaying menu:")
    print(system.display_menu())
    member_id = 2

    print("\nSelecting and adding menu items to cart:")
    
    # เลือกเมนูเบอร์เกอร์
    selected_menu = system.select_menu(1)
    print(f"Selected menu: {selected_menu}")
    
    # เพิ่มเบอร์เกอร์ 2 ชิ้นพร้อม Add-ons
    result = system.add_to_cart(member_id, selected_menu, 1, ["Bacon", "More_Patty"])
    print(f"Add to cart result: {result}")

    # เลือกเมนูเครื่องดื่ม
    selected_menu = system.select_menu(2)
    result = system.add_to_cart(member_id, selected_menu, 2, None)
    
    # ดูรายละเอียดของตะกร้า
    print("\nCart contents before removing an item:")
    print(system.watch_cart(member_id))

    # ลบสินค้าออกจากตะกร้า
    selected_menu = system.select_menu(1)
    print("\nRemoving an item from cart (Burger)...")
    system.remove_from_cart(member_id,selected_menu)
    # ดูรายละเอียดตะกร้าหลังลบ
    print("\nCart contents after removing Burger:")
    print(system.watch_cart(member_id))

    # ตรวจสอบยอดรวมของตะกร้า
    total_price = system.show_total_price(member_id)
    print(f"\nTotal price after removing Burger: ${total_price:.2f}")


    print("\nCart Summary ก่อนใช้คูปอง:")
    
    print(system.checkout(member_id))

    # ใช้คูปองลดราคา 10%
    coupon = system.show_user_coupon(member_id)
    index = 0 #Index ของ Dropdown เด้อครับพี่น้อง
    print(coupon)
    system.apply_coupon(member_id,coupon[index])
    total_price = system.show_total_price(member_id)
    print(f"\nc ${total_price:.2f}")
   
    
    # แสดงตะกร้าหลังใช้คูปอง
    print("\nCart Summary หลังใช้คูปอง:")
    print(system.checkout(member_id))
    print(f"Total = {total_price}")
    
    
    print(coupon)

    # กดยืนยันออเดอร์
    print("\nCreating Order...")
    # payment = CreditCard("1234567890123456", "12/25", "123")
    order_id = system.create_order(member_id)


    # # print("test")
    # # selected_menu = system.select_menu(1)
    # # result = system.add_to_cart(member_id, selected_menu, 2, ["Bacon", "More_Patty"])
    # # print(f"Add to cart result: {result}")
    # # print(member.get_cart().get_cart_details())
    

    # # print("\nCreating Order...")
    # # # payment = CreditCard("1234567890123456", "12/25", "123")
    # # print(member.create_order())

    print("\nOrder List:")
    for order in member.get_order_list():
        print(order)
    
    payment_method = CreditCard("1234567890123456", "12/25", "123")
    print(system.pay_order(member_id,order_id,payment_method))
    for order in member.get_order_list():
        print(order)
    point = member.get_point()
    print(system.exchange_point_to_coupon(member_id,point))
    print(member.get_coupon())
testrun(system, member)
