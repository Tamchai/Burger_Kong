# from fasthtml.common import *
# from dataclasses import dataclass
from fasthtml.common import * 
from routing import app, rt
import server
# from server import Member
# from server import Cart
# from server import CartItem
from server import *
# from all_menu import user_id
system = server.system
member = server.member
# current_user_id =
# total_price = 00
@rt('/view_cart/{current_user_id}', methods=["GET","POST"])
def view_cart(current_user_id : int):
    user = system.search_user_by_id(current_user_id)
    if user is None:
        return "Error: User not found", 404
    
    cart = user.get_cart()
    if cart is None:
        return "Error: Cart not found", 404
    
    user = system.search_user_by_id(current_user_id)
    return Container(
        Div(
            Div(
                Div(
                    Form(Button(
                        Img(src="https://i.imgur.com/fCpADUO.png", style="width: 50px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;",type="submit"),
                            action = "/home",method = "GET"
                    ),
                    H2("Burger Kong", style="color: #502314; margin: 0;"),
                    style="display: flex; align-items: center; gap: 10px;"
                ),
                Div(
                        Form(
                            Button(
                            Img(src="https://i.imgur.com/SwkvgTW.png",style="width: 40px; height: auto; margin-right: 15px;"),
                            style="background: none; border: none; cursor: pointer;", type = "submit"), action = f"/select_address/{current_user_id}", method = "GET"),
                        Form(Button(
                        Img(src="https://i.imgur.com/Xyhfm0Q.png", style="width: 40px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;", type = "submit"), action = f"####/{current_user_id}", method = "GET"),
                        Form(Button(
                            Img(src="https://i.imgur.com/JZR6dA6.png", style="width: 45px; height: auto;"),
                                style="background: none; border: none; cursor: pointer;", type = "submit"), action = f"/coupon_member/{current_user_id}", method = "GET"),
                        Form(Button(
                            Img(src="https://i.imgur.com/2eQjSEg.png", style="width: 45px; height: auto;"),
                                style="background: none; border: none; cursor: pointer;", type = "submit"), action = f"/view_cart/{current_user_id}", method = "POST"),
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
                            Form(Button("Add more",type="submit", style="background: #502314; color: white; padding: 5px 10px; border: none; border-radius: 10px; text-align: center;"),action="/home",method="GET"),
                            style="display: flex; justify-content: space-between; align-items: center; width: 98%;  padding-bottom: 10px;"
                        ),
                        Div(id="cart-items",
                            *[
                                Div(
                                # Div(f"{item.get_menu().get_name()} x {item.get_quantity()} ", 
                                #     style="font-size: 20px; font-weight: bold; color: #502314; padding: 5px;"),
                                Div(f"{item} ", 
                                    style="font-size: 20px; font-weight: bold; color: #502314; padding: 5px;"),   
                                Div(f"${item.get_total_price():.2f}",
                                    Button("Remove",
                                            hx_delete=f"/delete_cart_item/{current_user_id}/{item.get_menu().get_id()}",
                                           hx_target="#cart-items",
                                           hx_swap="outerHTML",
                                            type="submit",
                                            action="/refresh",
                                            style="background: #D00000; color: white; padding: 5px 10px; border: none; border-radius: 10px; text-align: center; margin-left: 10px;"),
                                    style="font-size: 20px; font-weight: bold; color: #502314; padding: 5px; gap 50px; display: flex; justify-content: space-between; align-items: center;"),
                                style="display: flex; justify-content: space-between; width: 100%; border-bottom: 1px solid rgba(80, 35, 20, 0.2); padding: 5px 0;"
                            ) 
                                for item in user.get_cart().get_item_list()],
                            style="flex-grow: 1; width: 98%; align-items: flex-start;  padding: 10px;"
                        ),
                        Div(
                            H3("Discount:", style="color: #502314;"),
                            Div(
    H2(f"Total: ${user.get_cart().calculate_total_price():.2f}", id="total", style="color: #D00000; font-weight: bold; margin-top: 10px;")
),  
                            Div(
                                Button("Checkout",style="font-size: 20px; font-weight: bold; background-color: #D00000; color: #ffffff; width: 50%; padding: 10px; border: none; display: block; margin: auto; border-radius: 10px;",onclick=f"window.location.href='/order_summary/{current_user_id}'"),
                                action =f"/order_summary/{current_user_id}", method = "GET",
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


@rt("/delete_cart_item/{current_user_id}/{item_id}", methods=["DELETE"])
def delete_cart_item(current_user_id: int, item_id: int):
    user = system.search_user_by_id(current_user_id)
    if user is None:
        return "Error: User not found", 404
    
    system.remove_from_cart(current_user_id, system.search_menu_by_id(item_id))
    
    cart = user.get_cart()
    total_price = cart.calculate_total_price() if cart else 0.00
    return Div(id="cart-items", *[
        Div(
            Div(f"{item} ", 
                style="font-size: 20px; font-weight: bold; color: #502314; padding: 5px;"),   
            Div(f"${item.get_total_price():.2f}",
                Button("Remove",
                       hx_delete=f"/delete_cart_item/{current_user_id}/{item.get_menu().get_id()}",
                       hx_target="#cart-items",
                       hx_swap="outerHTML",
                       style="background: #D00000; color: white; padding: 5px 10px; border: none; border-radius: 10px; margin-left: 10px;"),
                style="font-size: 20px; font-weight: bold; color: #502314; padding: 5px; display: flex; justify-content: space-between; align-items: center;"),
            style="display: flex; justify-content: space-between; width: 100%; border-bottom: 1px solid rgba(80, 35, 20, 0.2); padding: 5px 0;"
        ) for item in cart.get_item_list()                   
    ]), H2(f"Total: ${total_price:.2f}", id="total", hx_swap_oob="innerHTML", style="color: #D00000; font-weight: bold; margin-top: 10px;")

serve()