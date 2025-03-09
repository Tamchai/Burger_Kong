from fasthtml.common import *

app, rt = fast_app(live=True)

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
            H1("Order Summary", style="color: #502314; text-align: center; padding: 10px;"),
            Div(
                H3("Delivery to", style="color: #502314;"),
                Input(placeholder="Address", style="color: #000; background: #fff; width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 10px"),
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
                        Button("Add more", style="background: #502314; color: white; padding: 5px 10px; display: inline-block;"),
                        style="display: flex; align-items: center; justify-content: space-between;"
                    ),
                    Div(id="cart-items", children=[Div("No items in cart")]),
                    style="width: 50%; padding: 15px;"
                ),
                Div(
                    Div(
                        Div(
                            H3("Subtotal:", style="color: #502314; display: inline-block;"),
                            H3("0", style="color: #502314; float: right;"),
                            style="width: 100%;"
                        ),
                        Div(
                            H3("Delivery Fee:", style="color: #502314; display: inline-block;"),
                            H3("0", style="color: #502314; float: right;"),
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
        )
    )

serve()
