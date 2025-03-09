from fasthtml.common import *

app, rt = fast_app(live=True)

user_points = 1500

@rt('/')
def get():
    return Container(
        Div(
            Div(
                Div(
                    Button(
                        Img(src="https://i.imgur.com/fCpADUO.png", style="width: 50px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;"),
                    H2("Burger Kong", style="color: #502314; margin: 0;"),
                    style="display: flex; align-items: center; gap: 10px;"
                ),
                Div(
                    Button(
                        Img(src="https://i.imgur.com/Xyhfm0Q.png", style="width: 40px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;"),
                    Button(
                        Img(src="https://i.imgur.com/JZR6dA6.png", style="width: 45px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;"),
                    Button(
                        Img(src="https://i.imgur.com/2eQjSEg.png", style="width: 45px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;"),
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
        H1("Coupon Rewards", style="color: #502314; background: #f5ebdc; text-align: center; padding: 10px; padding-top: 70px;"),
        Div(
            Div(
                 Div(
                    H1("Coupon", style="color: #502314;"),
                    H3(f"Point: {user_points}", 
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
                Div(id="cart-items", children=[],
                    style="flex-grow: 1; width: 100%;"
                ),
                style="display: flex; flex-direction: column; width: 100%; height: 100%; flex-grow: 1;"
            ),
            style="display: flex; flex-direction: column; background: #f5ebdc; padding: 20px; border-radius: 30px; width: 75%; height: 90vh; margin: auto; border: 1px solid #502314;"
        ),

        style="background: #f5ebdc; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 20px;"
    )
)

serve()
