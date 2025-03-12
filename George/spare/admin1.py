from fasthtml.common import *
from routing import app, rt
import server
import admin_product
system = server.system  

@app.get('/admin')
def admin_home():
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
                        Form(
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
                                """,
                                type="submit"),
                                action= "/product_manager",
                                method="get"
                            ),
                        ), 
                    Div(
                        Form(
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
                                """,
                                type="submit"),
                                action= "/product_manager",
                                method="get"
                            )
                        ),
                    Div(
                        Form(
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
                                """,
                                type="submit"),
                                action= "/coupon_manager",
                                method="get"
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
            ),  style="margin-top: 2%; background: #f5ebdc; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 20px;"
        )
    )

# Remove or comment out the serve() call:
serve()
