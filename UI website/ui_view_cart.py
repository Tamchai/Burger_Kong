from fasthtml.common import *

app, rt = fast_app(live=True)

@rt('/')
def get():
    return Container(Body(
        H1("BurgerKong Cart", style="color: #502314; background: #f5ebdc; text-align: center; padding: 10px;"),
        Textarea(placeholder="Enter your menu", style="color: #000; width: 75%; height: 50px; background: white; border: 1px solid #502314; padding: 10px; border-radius: 10px; margin-top: 10px; margin-left:12%; white-space: nowrap; resize: none; overflow: hidden;"),
        Div(
            Div(
                Div(
                    H2("Your Order", style="color: #502314;"),
                    Button("Add more", style="background: #502314; color: white; padding: 5px 10px; border: none; border-radius: 10px; text-alian:center;"),
                    style="display: flex; justify-content: space-between; align-items: center; width: 100%; padding-bottom: 10px;"
                ),
                Div(id="cart-items", children=[],
                    style="flex-grow: 1; width: 100%;"
                ),
                Div(
                    H3("Discount:", style="color: #502314;"),
                    H2("Total:", id="total", style="color: #D00000; font-weight: bold; margin-top: 10px;"),
                    Div(
                        Button("Checkout", 
                               style="background-color: #D00000; color: #ffffff; width: 50%; padding: 10px; border: none; display: block; margin: auto; border-radius: 10px;"),
                        style="width: 100%; display: flex; justify-content: center; margin-top: 15px;"
                    ),
                    style="display: flex; flex-direction: column; width: 100%; padding-top: 15px; margin-top: auto;"
                ),
                style="display: flex; flex-direction: column; width: 100%; height: 100%; flex-grow: 1;"
            ),
            style="display: flex; flex-direction: column; background: #f5ebdc; padding: 20px; border-radius: 30px; width: 75%; height: 90vh; margin: auto; border: 1px solid #502314;"
        ),
        style="background: #f5ebdc; min-height: 100vh; display: flex; align-items: center; justify-content: center;"
    ))

serve()