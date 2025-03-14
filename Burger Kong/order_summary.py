from fasthtml.common import *
from routing import app, rt
import server
from server import Member, Cart, CartItem
import payment

system = server.system
discount_amount = 0  

@rt('/order_summary/{current_user_id}', methods=["GET", "POST"])
def order_summary(current_user_id: int):
    """Displays the order summary page."""
    print(f"Loading Order Summary for user: {current_user_id}") 

    user = system.search_user_by_id(current_user_id)
    if not user:
        print("Error: User not found")
        return "Error: User not found", 404

    cart = user.get_cart()
    address_list = user.get_address_list()
    global discount_amount

    total_price = cart.calculate_total_price() + 2 - discount_amount
    return Container(
        Div(
            Div(
                Div(
                    Form(Button(
                        Img(src="https://i.imgur.com/fCpADUO.png", style="width: 50px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;",type="submit"),action = "/home",method = "GET"),      
                    H2("Burger Kong", style="color: #502314; margin: 0;"),
                    style="display: flex; align-items: center; gap: 10px; "
                ),
                Div(
                        Form(
                            Button(
                            Img(src="https://i.imgur.com/SwkvgTW.png",style="width: 40px; height: auto; margin-right: 15px;"),
                            style="background: none; border: none; cursor: pointer;", type = "submit"), action = f"/select_address/{current_user_id}", method = "GET"),
                        Form(Button(
                        Img(src="https://i.imgur.com/Xyhfm0Q.png", style="width: 40px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;", type = "submit"), action = "####", method = "GET"),
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
            H1("Order Summary", style="color: #502314; text-align: center; padding: 15px;"),
            Form(
                Div(
                    H3("Delivery to", style="color: #502314;"),
                    Select(
                        *[Option(f"{address.get_name()} - {address.get_detail()}", id="address", name="address") for address in address_list],
                        name="address",
                        style="""
                            background: #fff; 
                            border: 1px solid #ccc; 
                            border-radius: 8px; 
                            padding: 10px; 
                            font-size: 16px;
                            color: #502314;
                        """
                    ),
                    style="""
                        background: #f5ebdc; 
                        padding: 20px; 
                        border-radius: 20px; 
                        margin-bottom: 20px; 
                        width: 80%; 
                        border: 2px solid #502314; 
                        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);
                        margin: auto;
                        margin-bottom: 10px;
                        overflow-y: auto;
                    """
                ),
                Div(
                    Div(
                        Div(
                            H3("Your Order", style="color: #502314; display: inline-block; margin-right: 10px;"),
                            style="display: flex; align-items: center; justify-content: space-between;"
                        ),
                        *[
                            Div(
                                Div(f"{item.get_menu().get_name()} x {item.get_quantity()}",
                                    style="font-size: 18px; font-weight: bold; color: #502314; padding: 8px;"),
                                Div(f"${item.get_total_price():.2f}",
                                    style="font-size: 18px; font-weight: bold; color: #502314; padding: 8px;"),
                                style="display: flex; justify-content: space-between; width: 100%; border-bottom: 1px solid #ddd; padding-bottom: 5px;"
                            )
                            for item in cart.get_item_list()
                        ],
                        style="width: 100%; padding: 20px; background: #f5ebdc; border-radius: 15px; overflow-y: auto;"
                    ),
                    Div(
                        Div(
                            Div(
                                Div(
                                    H3("Subtotal:", style="color: #502314; width: 150px; text-align: left;"),
                                    H3(f"${cart.calculate_total_price():.2f}", style="color: #502314;  flex: 1; text-align: right;"),
                                    style="display: flex; justify-content: space-between; width: 100%;"
                                ),
                                Div(
                                    H3("Delivery Fee:", style="color: #502314; width: 150px; text-align: left;"),
                                    H3("$2", style="color: #502314;  flex: 1; text-align: right;"),
                                    style="display: flex; justify-content: space-between; width: 100%;"
                                ),
                                style="""
                                    background: #f5ebdc; 
                                    padding: 15px; 
                                    border-radius: 10px; 
                                    width: 100%; 
                                    display: flex; 
                                    flex-direction: column; 
                                    gap: 10px;
                                    align-items: flex-start;
                                """
                            )
                        ),
                        H3("Coupon Discount", style="color: #502314; margin-top: 15px;text-align: left;"),
                        Select(Option(),
                            *[Option(f"{coupon.get_name()} - {coupon.get_discount()}%", value=coupon.get_name()) for coupon in user.get_coupon()],
                            name="coupon_discount",
                            id="coupon_discount",
                            hx_post="/update_total",
                            hx_trigger="change",
                            hx_target="#total",
                            hx_swap="innerHTML",
                            style="background: #fff; border: 1px solid #ccc; border-radius: 8px; padding: 10px; font-size: 16px; color: #502314;"
                        ),
                        H2(f"Total: ${total_price:.2f}", id="total", style="color: #D00000; font-weight: bold;"),
                        Button("Checkout", type="submit", style="background-color: #D00000; color: #ffffff; width: 100%; padding: 12px; border: none; border-radius: 8px; margin-top: 10px;"),
                        style="width: 100%;"
                    ),
                    style="""
                    display: flex; 
                    justify-content: space-between; 
                    background: #f5ebdc; 
                    padding: 15px; 
                    border-radius: 30px; 
                    width: 80%; 
                    margin: auto; 
                    margin-top: 20px; 
                    border: 1px solid #502314; 
                    gap: 20px; 
                    overflow-y: auto;
                    """),
                method="GET",
                action=f"/before_payment/{current_user_id}",
                style="background: #f5ebdc; padding: 20px; border-radius: 20px; width: 80%; margin: auto; margin-top: 30px; overflow-y: auto;"
            ),
            style="background: #f5ebdc; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding-top: 100px; overflow-y: auto;"
            )
)
            
@app.post("/update_total")
def update_total(coupon_discount: str = Form("0")):
    """Updates the total price when a coupon is applied."""
    global discount_amount
    current_user_id = server.current_user_id
    user = system.search_user_by_id(current_user_id)
    print(f"dfga: {coupon_discount}")  # Debugging
    if not user:
        print("Error: User not found in update_total")
        return "Error: User not found", 404
    cart = user.get_cart()
    subtotal = cart.calculate_total_price()
    delivery_fee = 2
    try:
        discount_percentage = float(coupon_discount)
    except ValueError:
        discount_percentage = 0.0

    discount_amount = subtotal * (discount_percentage / 100)
    total = subtotal + delivery_fee - discount_amount

    print(f"Updated total: ${total:.2f} (Discount: ${discount_amount:.2f})")  # Debugging

    return f"Total: ${total:.2f}"

@rt('/before_payment/{current_user_id}', methods=["GET"])
def before_payment_summary(current_user_id: int, address: str = "", coupon_discount: str = Form("0"), cutlery_value: str = "0", sauce_value: str = "0", message: str = ""):
    """Handles redirection to payment after confirming order summary."""
    print(f"Before payment processing for user: {current_user_id}")  # Debugging
    print("AAAAAAAAAAAAAAAA")
    print(f"AAAAA:  {coupon_discount}")  # Debuggin
    user = system.search_user_by_id(current_user_id)
    if not user:
        print("Error: User not found in before_payment")
        return "Error: User not found", 404
    cart = user.get_cart()
    coupon = system.show_user_coupon(current_user_id)
    print(coupon)
    # index = 0 #Index ของ Dropdown เด้อครับพี่น้อง
    # print(coupon)
    for each in coupon:
        if coupon_discount == each.get_name():
            print(each)
            index = coupon.index(each)
            print(index)
            system.apply_coupon(current_user_id,coupon[index])
    print("SUSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    # print(system.show_total_price(current_user_id))
    total_price = system.show_total_price(current_user_id)+2
    x = system.create_order(current_user_id)
    print(x)

    # if coupon_discount in coupon:
    #     index = coupon.index(coupon_discount)
    #     print(index)
    # system.apply_coupon(current_user_id,coupon[index])
    # Apply coupon discount properly
    # global discount_amount
    # try:
    #     discount_percentage = float(coupon_discount)
    #     discount_amount = cart.calculate_total_price() * (discount_percentage / 100)
    # except ValueError:
    #     discount_amount = 0.0

    # # Ensure total price is updated in the cart object
    # final_total = cart.calculate_total_price() + 2
    # print(f"Final Total before payment: ${final_total:.2f}")  # Debugging

    return RedirectResponse(f"/payment/{current_user_id}/{total_price}/{x.get_id()}")
serve()