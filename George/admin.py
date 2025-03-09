from fasthtml.common import *
from dataclasses import dataclass
from routing import app, rt  # Use the app and rt from routing.py
import server

system = server.system  

@rt('/admin')
def get():
    return Container(
        Div(
            Div(
                Button(
                    Img(src="https://i.imgur.com/fCpADUO.png", style="width: 60px; height: auto;"),
                    style="background: none; border: none; cursor: pointer;"
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
            Div(
                H2("Manager", style="color: #502314; text-align: center; margin-bottom: 10%;"),
                Div(
                    Div(
                        Button("View Customer",
                            style="""
                            font-weight: bold; 
                            font-size: 16px; 
                            color: #fff; 
                            text-align: center; 
                            background: #502314; 
                            border-radius: 5px; 
                            border: none; 
                            width: 100%;
                            margin-bottom: 10%;
                            """
                        ),
                    ),
                    Div(
                        Button("Product Manager",
                            style="""
                            font-weight: bold; 
                            font-size: 16px; 
                            color: #fff; 
                            text-align: center; 
                            background: #502314; 
                            border-radius: 5px; 
                            border: none; 
                            width: 100%;
                            margin-bottom: 5%;
                            """
                        ),
                    ),
                    Div(
                        Button("Coupon Manager",
                            style="""
                            font-weight: bold; 
                            font-size: 16px; 
                            color: #fff; 
                            text-align: center; 
                            background: #502314; 
                            border-radius: 5px; 
                            border: none; 
                            width: 100%;
                            margin-bottom: 5%;
                            """
                        ),
                    ),
                    style="""
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                    """
                ),
                style="""
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    background: #f5ebdc; 
                    padding: 2%; 
                    border-radius: 10px; 
                    width: 20%;
                    height: auto; 
                    border: 1px solid #502314; 
                    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3);
                    margin: auto;
                    position: relative;
                    top: -50px;
                """
            ),  
            style="margin-top: 2%; background: #f5ebdc; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 20px;"
        )
    )

# Remove or comment out the serve() call:
# serve()
