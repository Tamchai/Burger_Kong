from fasthtml.common import *
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
total_price = 0  # ตัวแปรเก็บราคาสุทธิ
payment_method = "-"  # ตัวแปรเก็บวิธีการชำระเงิน
credit_card_info = None  # ตัวแปรเก็บข้อมูลบัตรเครดิต
system = System()


app, rt = fast_app(live=True)
@rt("/total_price") 
def get_total_price_api():
        return "100"
    # return f"{system.get_total_price()} " อันนี้ของจริงตามหลัก
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
                    Img(src="https://i.imgur.com/Xyhfm0Q.png",
                        style="width: 40px; height: auto; margin-right: 15px;"),
                    Img(src="https://i.imgur.com/AcIDazc.png",
                        style="width: 40px; height: auto; margin-right: 15px;"),
                    Img(src="https://i.imgur.com/Kj7efMN.png",
                        style="width: 40px; height: auto; margin-right: 10px;"),
                    Img(src="https://i.imgur.com/2eQjSEg.png",
                        style="width: 40px; height: auto; margin-right: 20px;"),
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
            Div(
                H3("Payment", style="font-size: 36px;text-align: center; color: #502314;"),
                Form(
                    Group(
                        Div(
                            Label("ชื่อ",style="color: #502314; font-size: 18px; font-weight: bold;"),
                            Input(type="text", id="name", style="color: #000; background: #fff; padding: 8px; border-radius: 15px; border: 1px solid #502314;"),
                            style="display: flex; flex-direction: column; gap: 5px; width: auto; "
                        ),
                        Div(
                            Label("เบอร์โทรศัพท์มือถือ",style="color: #502314; font-size: 18px; font-weight: bold;"),
                            Input(type="text", id="No", style="color: #000; background: #fff;padding: 8px; border-radius: 15px; border: 1px solid #502314;"),
                            style="display: flex; flex-direction: column; gap: 5px; width: auto;"
                        ),
                        style="display: flex; gap: 15px; background: #fff; flex-direction: column; padding: 15px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);"
                    ),
                    H3("เลือกวิธีการชำระเงิน", style="font-size: 24px; color: #502314; margin-top: 20px;"),
                    Group(
                        Div(
                            Label("บัตรเครดิต/เดบิต", style="color: #502314; font-size: 18px; font-weight: bold;"),
                            Input(type="radio", id="credit", name="payment", value="credit", style="background:#fff; margin-left: 5px;"),
                            style="display: flex; flex-direction: column; gap: 5px; width: auto;"
                        ),  
                            Div( 
                                        Label("หมายเลขบัตรเครดิต", style="color: #502314; font-size: 18px; font-weight: bold;"),
                                        Input(type="text", id="card-number", placeholder="1234 5678 1234 5678", style="color: #502314;background: #fff; padding: 8px; border-radius: 15px; border: 1px solid #502314;"),
                                        Label("วันหมดอายุ", style="color: #502314; font-size: 18px; font-weight: bold;"), 
                                        Input(type="text", id="expiry-date", placeholder="MM/YY", style="color: #502314;background: #fff; padding: 8px; border-radius: 15px; border: 1px solid #502314;"),
                                        Label("CVV", style="color: #502314; font-size: 18px; font-weight: bold;"),
                                        Input(type="text", id="cvv", placeholder="123", style="color: #502314;background: #fff; padding: 8px; border-radius: 15px; border: 1px solid #502314;"), 
                                        id="credit-options",
                                        style="display: none; background: #fff; padding: 8px; border-radius: 15px; border: 1px solid #502314;"    
                            ),
                        Div( 
                            Label("QRCODE", style="color: #502314; font-size: 18px; font-weight: bold;"),
                            Input(type="radio", id="qrcode", name="payment", value="QRCODE", style="background:#fff; margin-left: 5px;"),
                            style="display: flex; flex-direction: column; gap: 5px; width: auto;"
                        ),
                         Div(
                        Label("เลือกประเภท QRCODE", style="display: none;color: #502314; font-size: 18px; font-weight: bold;"),
                       
                           Img(src="https://i.imgur.com/6uY8X50.jpeg",
                            id="qrcode-options",
                            style="display: none; background: #fff; padding: 8px; border-radius: 15px; border: 1px solid #502314;"
                        ),
                        style="display: flex; flex-direction: column; gap: 5px; width: auto;"
                    ),
                        style="display: flex; flex-direction: column; gap: 15px; background: #fff; padding: 15px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);"
                    ),
         Div(
    Label(Strong("ราคาสุทธิ: "), 
    Span("...", id="total_price", hx_get="/total_price", hx_trigger="load"),  # ดึงราคาอัตโนมัติ
    " บาท",
    style="font-size: 24px; text-align: center; color: #502314;")
),         # เพิ่ม dropdown ที่จะทำให้แสดงเมื่อเลือก QRCODE
                    Button("สั่งอาหาร", type="submit", style="background: #502314; color: white; font-weight: bold; padding: 10px 20px; border: none; border-radius: 20px; cursor: pointer; margin-top: 20px;"),
                    method="post",
                    action="/submit",
                    style="max-width: 500px; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);"
                    
                )
            ),
            style="background: #f5ebdc; padding: 20px; min-height: 100vh; margin-top: 80px;"
          
        ),
        Script("""
        document.getElementById('qrcode').addEventListener('change', function() {
    var qrcodeOptions = document.getElementById('qrcode-options');
    var creditOptions = document.getElementById('credit-options');
    if (this.checked) {
        qrcodeOptions.style.display = 'block';
        creditOptions.style.display = 'none';
    }
});

document.getElementById('credit').addEventListener('change', function() {
    var qrcodeOptions = document.getElementById('qrcode-options');
    var creditOptions = document.getElementById('credit-options');
    if (this.checked) {
        qrcodeOptions.style.display = 'none';
        creditOptions.style.display = 'block';
    }
});

        """)
    )

@rt("/submit")
def post(name: str, No: str, payment: str, card_number: str = "", expiry_date: str = "", cvv: str = ""):
    if payment_method == "Credit Card" and not card_number and payment_method ==  "":
        return "Error: ต้องกรอกหมายเลขบัตรเครดิต"
    return f"ต้องลิ้งไปหน้าโชว์ออเดอร์ ยังไม่ทำ Order Placed Successfully :ยืนยัน: {name}, {No}, วิธีชำระเงิน: {payment}, ราคาสุทธิ: ${get_total_price_api()}"

serve()
