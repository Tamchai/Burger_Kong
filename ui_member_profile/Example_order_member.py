from fasthtml.common import *
from dataclasses import dataclass

app, rt = fast_app(live=True)

mock_members = [
    {
        "orders": [
            {"name": "Burger King Combo", "quantity": 1, "price": 150},
            {"name": "Cheese Fries", "quantity": 2, "price": 50}
        ],
        "active": True
    },
    {
        "orders": [
            {"name": "Spicy Chicken Burger", "quantity": 1, "price": 120},
            {"name": "Onion Rings", "quantity": 1, "price": 80}
        ],
        "active": False
    },
    {
        "orders": [
            {"name": "Double Cheeseburger", "quantity": 1, "price": 180},
            {"name": "Large Soda", "quantity": 2, "price": 40}
        ],
        "active": True
    }
]

@rt('/')
def get():
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
                            style="background: none; border: none; cursor: pointer;", type = "submit"),),
                        Form(Button(
                        Img(src="https://i.imgur.com/Xyhfm0Q.png", style="width: 40px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;", type = "submit"), action = "####", method = "GET"),
                        Form(Button(
                            Img(src="https://i.imgur.com/JZR6dA6.png", style="width: 45px; height: auto;"),
                                style="background: none; border: none; cursor: pointer;", type = "submit"), ),
                        Form(Button(
                            Img(src="https://i.imgur.com/2eQjSEg.png", style="width: 45px; height: auto;"),
                                style="background: none; border: none; cursor: pointer;", type = "submit"),),
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
            H1("Your Orders", style="color: #502314; text-align: center; padding: 10px; margin-top: 80px;"),
            Div(
                *[
                    Div(
                        Div(
                            H2("Order #[num]", style="color: #502314;"),
                            Button(
                                "Delete",
                                style="background: #D00000; color: white; padding: 5px 10px; border-radius: 10px; border: 1px solid #502314; cursor: pointer;",
                                **{"hx-get": "/manage_order", "hx-target": "#order-section"}
                            ),
                            style="display: flex; justify-content: space-between; align-items: center; width: 100%; padding-bottom: 10px;"
                        ),
                        Div(
                            *[
                                Div(
                                    f"{order['name']} - {order['quantity']}x | {order['price']} $",
                                    style="font-size: 18px; font-weight: bold; color: #502314; padding: 5px;"
                                ) for order in member["orders"]
                            ],
                            style="padding-left: 10px;"
                        ),
                        H3(
                            f"Total Price: {sum(order['quantity'] * order['price'] for order in member['orders'])} $",
                            style=""" 
                                color: #502314; 
                                padding: 5px 10px; 
                                border-radius: 10px; 
                                
                            """
                        ),
                        H3(
                            "Paying" if member["active"] else "Completed",
                            style="""
                                background: #502314; 
                                color: white; 
                                padding: 5px 10px; 
                                border-radius: 10px; 
                                text-align: center;
                            """
                        ),
                        style="""
                            background: white; 
                            padding: 20px; 
                            border-radius: 15px; 
                            width: 80%; 
                            text-align: left; 
                            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
                            margin: 1%;
                        """
                    ) for member in mock_members
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
