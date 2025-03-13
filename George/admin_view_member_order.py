from fasthtml.common import *
from dataclasses import dataclass
from routing import app, rt
import server
import admin
system = server.system     
from server import *

@rt('/admin_view_member_order', methods=["GET", "POST"])
def get():
    member_list = system.get_user_list()
    return Container(
        Div(
            Button(
                Img(src="https://i.imgur.com/fCpADUO.png", style="width: 60px; height: auto;"),
                style="background: none; border: none; cursor: pointer;"
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
            H1("Member Orders", style="color: #502314; text-align: center; padding: 10px; margin-top: 80px;"),
            Div(
                *[
                    Div(
                        *[(
                                Div(
                                    H2(member.get_name(), style="color: #502314;"),
                                    style="color: #502314; display: flex; justify-content: space-between; align-items: center; width: 100%; padding-bottom: 10px;"
                                ),
                                Div(
                                        Div(
                                            f"Order ID : {order.get_id()}",
                                            style="font-size: 18px; font-weight: bold; color: #502314; padding: 5px;"
                                        ),
                                        Div(
                                            f"Order Detail : ",
                                            *[P(each_order) for each_order in order.get_cart_items()],
                                            style="font-size: 18px; font-weight: bold; color: #502314; padding: 5px;"
                                        ),style="padding-left: 10px;"
                                ),
                                Div(H3(
                                    f"Total Price: {order.get_total_price()+2} $",
                                    style=""" 
                                        color: #502314; 
                                        padding: 5px 10px; 
                                        border-radius: 10px; 
                                        
                                    """
                                )),
                                H3(
                                    f"{order.get_status().capitalize()}",
                                    style="""
                                        background: #502314; 
                                        color: white; 
                                        padding: 5px 10px; 
                                        border-radius: 10px; 
                                        text-align: center;
                                    """
                            ) )for order in member.get_order_list()
                        ],
                        style="""
                            background: white; 
                            padding: 20px; 
                            border-radius: 15px; 
                            width: 80%; 
                            text-align: left; 
                            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
                            margin: 1%;
                        """
                    
                    ) for member in member_list if isinstance(member, Member)
                ],
                style="""
                    display: flex; 
                    flex-direction: column; 
                    align-items: center; 
                    justify-content: center; 
                    background: #f5ebdc; 
                    padding: 20px; 
                    border-radius: 30px; 
                    width: 90%; 
                    margin: auto; 
                    border: 1px solid #502314;
                """
            ),
            style="background: #f5ebdc; min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 20px;"
        )
    )


serve()
