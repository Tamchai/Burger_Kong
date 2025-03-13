from fasthtml.common import *
from routing import app, rt
import server
from server import Member, Cart, CartItem
import payment

system = server.system
discount_amount = 0  # Global discount tracking

@rt('/order_summary/{current_user_id}', methods=["GET", "POST"])
def order_summary(current_user_id: int):
    """Displays the order summary page."""
    print(f"Loading Order Summary for user: {current_user_id}")  # Debugging

    user = system.search_user_by_id(current_user_id)
    if not user:
        print("Error: User not found")
        return "Error: User not found", 404

    cart = user.get_cart()
    address_list = user.get_address_list()
    global discount_amount

    # Calculate total including discount
    total_price = cart.calculate_total_price() + 2 - discount_amount

    return Container(
        H1("Order Summary", style="color: #502314; text-align: center; padding: 10px;"),
        Form(  # 🛠 Wrapped in a form to ensure proper form submission
            Div(
                H3("Delivery to", style="color: #502314;"),
                Select(
                    *[Option(f"{address.get_name()} - {address.get_detail()}", id="address", name="address") for address in address_list],
                    name="address",  # Added name to ensure form submission
                    style="background: #fff; border: 1px solid #ccc; border-radius: 5px; padding: 8px; font-size: 16px; color: #502314;"
                ),
                style="background: #f5ebdc; padding: 15px; border-radius: 30px; width: 60%; margin: auto;"
            ),
            Div(
                H3("Your Order", style="color: #502314;"),
                *[
                    Div(
                        Div(f"{item.get_menu().get_name()} x {item.get_quantity()}",
                            style="font-size: 20px; font-weight: bold; color: #502314; padding: 5px;"),
                        Div(f"${item.get_total_price():.2f}",
                            style="font-size: 20px; font-weight: bold; color: #502314; padding: 5px;"),
                        style="display: flex; justify-content: space-between; width: 100%; border-bottom: 1px solid #ccc;"
                    )
                    for item in cart.get_item_list()
                ],
                style="width: 50%; padding: 15px;"
            ),
            Div(
                H3(f"Subtotal: ${cart.calculate_total_price():.2f}", style="color: #502314;"),
                H3("Delivery Fee: $2", style="color: #502314;"),
                H3(f"Discount: ${discount_amount:.2f}", style="color: #502314;"),
                H2(f"Total: ${total_price:.2f}", id="total", style="color: #D00000; font-weight: bold;"),
                Select(
                    *[Option(f"{coupon.get_name()} - {coupon.get_discount()}%", value=coupon.get_name()) for coupon in system.get_coupon_list()],
                    name="coupon_discount",
                    id="coupon_discount",
                    hx_post="/update_total",
                    hx_trigger="change",
                    hx_target="#total",
                    hx_swap="innerHTML",
                    style="background: #fff; border: 1px solid #ccc; border-radius: 5px; padding: 8px; font-size: 16px; color: #502314;"
                ),
                Button("Checkout", type="submit",
                       style="background-color: #D00000; color: #ffffff; width: 100%; padding: 10px; border: none;"),
                action=f"/before_payment/{current_user_id}", method="GET",  # 🛠 Corrected form submission
                style="width: 50%; padding: 15px; background: #f5ebdc; border-radius: 30px;"
            ),
            method="GET",  # 🛠 Added method for proper request
            action=f"/before_payment/{current_user_id}"  # 🛠 Ensures form redirects to the right endpoint
        ),
        style="background: #f5ebdc; min-height: 100vh; padding-top: 120px;"
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