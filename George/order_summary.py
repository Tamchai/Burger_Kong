from fasthtml.common import *
from routing import app, rt
import server
from server import Member
from server import Cart
from server import CartItem 
system = server.system 

@rt('/order_summary/{current_user_id}', methods=["GET","POST"])
def order_summary(current_user_id:int):
    user = system.search_user_by_id(current_user_id)
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
            H1("Order Summary", style="color: #502314; text-align: center; padding: 10px;"),
            Div(
                H3("Delivery to", style="color: #502314;"),
                Select(
                    children=[],
                    style="""
                        background: #fff; 
                        border: 1px solid #ccc; 
                        border-radius: 5px; 
                        padding: 8px; 
                        font-size: 16px;
                            color: #502314;
                    """
                ),
                style="""
                    background: #f5ebdc; 
                    padding: 15px; 
                    border-radius: 30px; 
                    margin-bottom: 20px; 
                    width: 60%; 
                    border: 1px solid #502314; 
                    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.5);
                    margin: auto;
                """
            ),
            Div(
                Div(
                    Div(
                        H3("Your Order", style="color: #502314; display: inline-block; margin-right: 10px;"),
                        Form(Button("Add more", style="background: #502314; color: white; padding: 5px 10px; display: inline-block;"),action="/home",method="GET"),
                        style="display: flex; align-items: center; justify-content: space-between;"
                    ),
                    Div(
                        *[
                                Div(
                                Div(f"{item.get_menu().get_name()} x {item.get_quantity()} ", 
                                    style="font-size: 20px; font-weight: bold; color: #502314; padding: 5px;"),
                                Div(f"${item.get_total_price():.2f}",
                                    style="font-size: 20px; font-weight: bold; color: #502314; padding: 5px; gap 50px; display: flex; justify-content: space-between; align-items: center;"),
                                style="display: flex; justify-content: space-between; width: 100%; border-bottom: 1px solid rgba(80, 35, 20, 0.2); padding: 5px 0;"
                            ) 
                                for item in user.get_cart().get_item_list()]
                    ),
                    style="width: 50%; padding: 15px;"
                ),
                Div(
                    Div(
                        Div(
                            H3("Subtotal: ", style="color: #502314; display: inline-block;"),
                            H3(user.get_cart().calculate_total_price(), style="color: #502314; float: right;"),
                            style="width: 100%;"
                        ),
                        Div(
                            H3("Delivery Fee:", style="color: #502314; display: inline-block;"),
                            H3(2, style="color: #502314; float: right;"),
                            style="width: 100%;"
                        ),
                        Div(
                            H3("Discount:", style="color: #502314; display: inline-block;"),
                            H3("0", style="color: #502314; float: right;"),
                            style="width: 100%;"
                        ),
                        style="background: #f5ebdc; width: 100%;"
                    ),
                        H3("Coupon Discount", style="color: #502314; margin-right: 10px;"),
                        Select(
                            *[Option(f"{coupon.get_name()} - {coupon.get_discount()}%",id = coupon.get_discount(), name = coupon.get_discount()) for coupon in system.get_coupon_list()]
                            ,
                            style=""" 
                                background: #fff; 
                                border: 1px solid #ccc; 
                                border-radius: 5px; 
                                padding: 8px; 
                                font-size: 16px;
                                color: #502314;
                            """
                        ),
                    H3("Additional Message", style="color: #502314;"),
                    Label(CheckboxX(id="cutlery"), "Cutlery", style="color: #502314; font-weight: bold;"),
                    Label(CheckboxX(id="sauce"), "Sauce", style="color: #502314; font-weight: bold;"),
                    Textarea(placeholder="Additional Message", style="background: #fff; width: 100%; height: 100px; margin-top: 5px; border: 1px solid #ccc; color: #000;"),
                    H2("Total:0.00$", id="total", style="color: #D00000; font-weight: bold;"),
                    Button("Checkout", style="background-color: #D00000; color: #ffffff; width: 100%; margin-top: 10px; padding: 10px; border: none;"),
                    style="width: 50%; padding: 15px;"
                ),
                style="display: flex; justify-content: space-between; background: #f5ebdc; padding: 15px; border-radius: 30px; width: 60%; margin: auto; margin-top: 20px; border: 1px solid #502314;"
            ),
        
            style="background: #f5ebdc; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding-top: 120px;"
        ),
    Footer(
        Div(
            H3("Contact Us", style="color: #fff; text-align: center; margin-bottom: 10px;"),
            Div("For inquiries, please visit our website or contact our customer service.", style="color: #fff;"),
        ),
             style=""" 
                display: flex;
                justify-content: center;
                align-items: center;
                background: #502314;
                padding: 15px;
                width: 100%;
                position: absolute;
                margin-top: 10px;
                left: 0;
            """
        ),
)

serve()
