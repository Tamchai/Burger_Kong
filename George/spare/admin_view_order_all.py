from dataclasses import dataclass
from fasthtml.common import *
from routing import app, rt
import server
# import admin_product
system = server.system 


# Mockup member 
@dataclass
class Cart:
    def get_item_list(self):
        return ["Item 1", "Item 2", "Item 3"]

@dataclass
class Member:
    cart = Cart()
    def get_cart(self):
        return self.cart

member = Member() 

@app.get('/admin_view_order_all')
def order_all():
    return Container(
        Div(
            Div(
                Button(
                    Img(src="https://i.imgur.com/fCpADUO.png", style="width: 60px; height: auto;"),
                    style="background: none; border: none; cursor: pointer;",
                    type = "button",
                    onclick = "history.back()"
                ),
            ),
            style="""
                width: 100%; 
                background: #f5ebdc; 
                padding: 15px; 
                border-bottom: 2px solid #502314;
                position: fixed; 
                top: 0; 
                left: 0;  
                z-index: 1000;
                box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.5);
                text-align: center;
            """
        ),
        Body(
            H1("View Order All", style="color: #502314; background: #f5ebdc; text-align: center; padding: 10px; padding-top: 70px;"),
            Div(
                Div(
                    Div(
                        H1("Order", style="color: #502314;"),
                        H3("Active",
                            style="""
                            background: #502314; 
                            color: white; 
                            padding: 5px 10px; 
                            border: none; 
                            border-radius: 10px; 
                            text-align: center;
                            """),
                        style="display: flex; justify-content: space-between; align-items: center; width: 100%; padding-bottom: 10px;"
                    ),
                    Div(id="cart-items",
                        *[
                            Div(
                                Div(f"Order#1",style="font-size: 20px; font-weight: bold; color: #502314; padding: 5px;"),
                                Div(
                                    Div(f"{item}", 
                                        style="font-size: 20px; font-weight: bold; color: #502314; padding: 5px;"),
                                    Button("Remove", style="background: #D00000; color: white; padding: 5px 10px; border: none; border-radius: 10px; text-align: center; margin-left: 10px;"),
                                    style="display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid rgba(80, 35, 20, 0.2);"
                                ),
                            style="padding: 10px 0; border-bottom: 1px solid rgba(80, 35, 20, 0.2);" 
                            )
                            for item in member.get_cart().get_item_list()
                        ],
                        style="flex-grow: 1; width: 98%; align-items: flex-start; padding: 10px;"
                    ),
                    style="flex-grow: 1; width: 100%;"
                ),
                style="display: flex; flex-direction: column; background: #f5ebdc; padding: 20px; border-radius: 30px; width: 75%; height: 90vh; margin: auto; border: 1px solid #502314;"
            ),
            style="margin-top: 3%; background: #f5ebdc; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 20px;"
        )
    )

serve()
