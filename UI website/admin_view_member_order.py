from fasthtml.common import *
from dataclasses import dataclass

app, rt = fast_app(live=True)

# Mock Data for Members
mock_members = [
    {
        "name": "John Doe",
        "orders": ["Burger King Combo", "Cheese Fries"],
        "active": True
    },
    {
        "name": "Jane Smith",
        "orders": ["Spicy Chicken Burger", "Onion Rings"],
        "active": False
    },
    {
        "name": "Alex Johnson",
        "orders": ["Double Cheeseburger", "Large Soda"],
        "active": True
    }
]

@rt('/')
def get():
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
                        Div(
                        H2(member["name"], style="color: #502314;"),
                        Button(
                            "Delete",
                            style="background: #D00000; color: white; padding: 5px 10px; border-radius: 10px; border: 1px solid #502314; cursor: pointer;",
                            **{"hx-get": "/manage_order", "hx-target": "#order-section"}
                            ),
                        style="display: flex; justify-content: space-between; align-items: center; width: 100%; padding-bottom: 10px; "
                        ),
                        Div(
                            *[
                                Div(
                                    f"{order}",
                                    style="font-size: 16px; font-weight: bold; color: #502314; padding: 5px;"
                                ) for order in member["orders"]
                            ],
                            style="padding-left: 10px;"
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
