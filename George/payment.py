from fasthtml.common import *
from routing import app, rt
import server
# from server import Member, Cart, CartItem
system = server.system 
from server import Order
from server import User
from server import CreditCard
from server import QRCode
from server import Payment
import order_summary
@rt("/payment/{current_user_id}/{total_price}/{order_id}", methods=["GET", "POST"])
def get(current_user_id:  int,total_price: float, order_id:int ):
    # target_order = ''
    # member = system.search_user_by_id(current_user_id)
    # order_user_list = member.get_order_list()
    # for order in order_user_list:
    #     if order.get_id() == order_id:
    #         target_order = order
    # print(target_order)
            
            
    
    return Container(
        Div(
            Div(
                Div(
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
                            Input(type="text", id="name", style="color: #000; background: #fff; padding: 8px; border-radius: 15px; border: 1px solid #502314;", requied = True),
                            style="display: flex; flex-direction: column; gap: 5px; width: auto; "
                        ),
                        Div(
                            Label("เบอร์โทรศัพท์มือถือ",style="color: #502314; font-size: 18px; font-weight: bold;"),
                            Input(type="text", id="tel", style="color: #000; background: #fff;padding: 8px; border-radius: 15px; border: 1px solid #502314;", requied = True),
                            style="display: flex; flex-direction: column; gap: 5px; width: auto;"
                        ),
                        style="display: flex; gap: 15px; background: #fff; flex-direction: column; padding: 15px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);"
                    ),
                    H3("เลือกวิธีการชำระเงิน", style="font-size: 24px; color: #502314; margin-top: 20px;"),
                    Group(
                        Div(
                            Label("บัตรเครดิต/เดบิต", style="color: #502314; font-size: 18px; font-weight: bold;"),
                            Input(type="radio", id="credit", name="payment", value="CREDIT", style="background:#fff; margin-left: 5px;", requied = True),
                            style="display: flex; flex-direction: column; gap: 5px; width: auto;"
                        ),  
                            Div( 
                                        Label("หมายเลขบัตรเครดิต", style="color: #502314; font-size: 18px; font-weight: bold;"),
                                        Input(type="text", id="card-number", placeholder="1234 5678 1234 5678", style="color: #502314;background: #fff; padding: 8px; border-radius: 15px; border: 1px solid #502314;", requied = True),
                                        Label("วันหมดอายุ", style="color: #502314; font-size: 18px; font-weight: bold;", requied = True), 
                                        Input(type="text", id="expiry-date", placeholder="MM/YY", style="color: #502314;background: #fff; padding: 8px; border-radius: 15px; border: 1px solid #502314;"),
                                        Label("CVV", style="color: #502314; font-size: 18px; font-weight: bold;", requied = True),
                                        Input(type="text", id="cvv", placeholder="123", style="color: #502314;background: #fff; padding: 8px; border-radius: 15px; border: 1px solid #502314;"), 
                                        id="credit-options",
                                        style="display: none; background: #fff; padding: 8px; border-radius: 15px; border: 1px solid #502314;"    
                            ),
                        Div( 
                            Label("QRCODE", style="color: #502314; font-size: 18px; font-weight: bold;"),
                            Input(type="radio", id="qrcode", name="payment", value="QRCODE", style="background:#fff; margin-left: 5px;", requied = True),
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
    Label(Strong(f"ราคาสุทธิ: {total_price}"), 
    Span("...", id="total_price", hx_get="/total_price", hx_trigger="load"),  # ดึงราคาอัตโนมัติ
    " บาท",
    style="font-size: 24px; text-align: center; color: #502314;")
),
                    Button("สั่งอาหาร", type="submit", style="background: #502314; color: white; font-weight: bold; padding: 10px 20px; border: none; border-radius: 20px; cursor: pointer; margin-top: 20px;"),
                    method="GET",
                    action=f"/submit/{current_user_id}/{order_id}",
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
    }});""")
)

@rt("/submit/{current_user_id}/{order_id}", methods=["GET", "POST"])
def get(current_user_id:int,order_id:int,name: str, tel: str, payment: str, card_number = "", expiry_date: str = "", cvv: str = ""):
    print("\nCreating Order...")
    # payment = CreditCard("1234567890123456", "12/25", "123")
    # order_id = system.create_order(user_id)
    # print(f"aaaaaaa{order_id.get_id()}")
    # print(f"aaaaaaa{order_id.get_total_price()}")
    member = system.search_user_by_id(current_user_id)
    for order in member.get_order_list():
        print(order.get_id())
        print(order_id)
        if order.get_id() == order_id:
            print("yay")
            print(order)
            orders = order
            break
        else :print("tak")
    # global order
    if payment == "CREDIT" and not (card_number and expiry_date and cvv):
        credit_card = CreditCard(card_number, expiry_date, cvv)
        system.pay_order(current_user_id,orders, credit_card)
        return "Success",RedirectResponse("/home")

serve()