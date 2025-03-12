from fasthtml.common import *
from routing import app, rt
import server
from server import Member
system = server.system 


# user_points = 1500

@app.get('/coupon_member/{current_user_id}')
def coupon_member(current_user_id : int):
    # global user_id
    user = system.search_user_by_id(current_user_id)
    return Container(
        Div(
            Div(
                Div(
                    Form(Button(
                        Img(src="https://i.imgur.com/fCpADUO.png", style="width: 50px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;",type="submit"
                            ),action = "/home", method = "GET"
                            
                        ),
                    H2("Burger Kong", style="color: #502314; margin: 0;"),
                    style="display: flex; align-items: center; gap: 10px;"
                ),
                Div(
                        Form(
                            Button(
                            Img(src="https://i.imgur.com/SwkvgTW.png",style="width: 40px; height: auto; margin-right: 15px;"),
                            style="background: none; border: none; cursor: pointer;", type = "submit"), action = f"/select_address/{current_user_id}", method = "GET"),
                        Form(Button(
                        Img(src="https://i.imgur.com/Xyhfm0Q.png", style="width: 40px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;", type = "submit"), action = f"/####/{current_user_id}", method = "GET"),
                        Form(Button(
                            Img(src="https://i.imgur.com/JZR6dA6.png", style="width: 45px; height: auto;"),
                                style="background: none; border: none; cursor: pointer;", type = "submit"), action = f"/coupon_member/{current_user_id}", method = "GET"),
                        Form(Button(
                            Img(src="https://i.imgur.com/2eQjSEg.png", style="width: 45px; height: auto;"),
                                style="background: none; border: none; cursor: pointer;", type = "submit"), action = f"/view_cart/{current_user_id}", method = "POST"),
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
                    H3(f"Point: {user.get_point()}", 
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
