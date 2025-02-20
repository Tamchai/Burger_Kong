from fasthtml.common import *

app, rt = fast_app(live=True)

@rt('/')
def get():
    return Container(Body(
        H1("Order Summary", style="color: #502314; background: #f5ebdc; text-align: center; padding: 10px;"),
        Div(
            H3("Delivery to", style="color: #502314;"),
            Input(placeholder="Address", style="background: #fff; width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 10px"),
            style="background: #f5ebdc; padding: 10px; border-radius: 20px; margin-bottom: 2px; width: 60%; margin: auto; border: 1px solid #502314; box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.5);"
        ),
        Div(
            Div(
                Div(
                    H3("Your Order", style="color: #502314; display: inline-block; margin-right: 10px;"),
                    Button("Add more", style="background: #502314; color: white; padding: 5px 10px; display: inline-block;"),
                    style="display: flex; align-items: center; justify-content: space-between;"
                ),
                Div(id="cart-items", children=[Div("No items in cart")]),
                style="width: 50%; padding: 15px;"
            ),
            Div(
                H3("Subtotal:", id="subtotal", style="color: #502314; display: inline-block margin-right: 10px;"),
                H3("0",style="color: #502314; padding: 5px 10px; display: inline-block;"),
                H3("Delivery Fee:", style="color: #502314;"),
                H3("Discount:", style="color: #502314;"),
                H3("Coupon Discount", style="color: #502314;"),
                Select([Option("Select coupon", value="", style="color: #D00000; border-radius: 10px")], style="background: #fff; width:100%; margin-top:5px;"),
                H3("Additional Message", style="color: #502314;"),
                Label(CheckboxX(id="cutlery"), "Cutlery",style="color: #502314;"),
                Label(CheckboxX(id="sauce"), "Sauce",style="color: #502314;"),
                Textarea(placeholder="Additional Message", style="background: #fff; width: 100%; height: 50px; margin-top: 5px; border: 1px solid #ccc; color: #000;"),
                H2("Total:", id="total", style="color: #D00000; font-weight: bold;"),
                Button("Checkout", style="background-color: #D00000; color: #ffffff; width: 100%; margin-top: 10px; padding: 10px; border: none;"),
                style="width: 50%; padding: 15px;"
            ),
            style="display: flex; justify-content: space-between; background: #f5ebdc; padding: 15px; border-radius: 30px; width: 60%; margin: auto;margin-top: 20px; border: 1px solid #502314;"
        ),
         style="background: #f5ebdc; min-height: 100vh; display: flex; align-items: center; justify-content: center;"
    )
)

serve()
