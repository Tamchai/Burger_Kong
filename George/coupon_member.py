from fasthtml.common import *
from routing import app, rt
import server
from server import Member
system = server.system 


# user_points = 1500

@rt('/coupon_member/{current_user_id}',methods=["GET","POST"])
def coupon_member(current_user_id : int):
    coupon_list = system.get_coupon_list()
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
                    Table(
                        Thead(
                            Tr(
                                Th("Coupon Code", style="font-weight: bold; font-size: 24px; text-align: center; background: none; color: #502314; padding: 10px; border: 1px none;"),
                                Th("Discount", style="font-weight: bold; font-size: 24px; text-align: center; background: none; color: #502314; padding: 10px; border: 1px none;"),
                                Th("Expire", style="font-weight: bold; font-size: 24px; text-align: center; background: none; color: #502314; padding: 10px; border: 1px none;"),
                                Th("Action", style="font-weight: bold; font-size: 24px; text-align: center; background: none; color: #502314; padding: 10px; border: 1px none;")
                            )
                        ),
                        Tbody( 
                            *[
                                Tr(
                                    Td(coupon.get_name(),style="font-weight: normal; font-size: 18px; color: #502314; background: #f5ebdc; padding: 8px; border: 1px none; text-align: center;"),
                                    Td(coupon.get_discount(),style="font-weight: normal; font-size: 18px; color: #502314; background: #f5ebdc; padding: 8px; border: 1px none; text-align: center;"),
                                    Td(coupon.get_expire_date(),style="font-weight: normal; font-size: 18px; color: #502314; background: #f5ebdc; padding: 8px; border: 1px none; text-align: center;"),
                                    Td(
                                Button("Exchange",
                                    hx_delete=f"/use_coupon/{current_user_id}/{coupon.get_name()}",  # ✅ Use hx_delete for proper HTTP semantics
                                    hx_target=f"result",  # ✅ Targets the table body
                                    hx_swap="outerHTML",  # ✅ Replaces only the table body, not the full page
                                    style="background: #D00; color: white; border: none; padding: 5px 10px; border-radius: 5px; cursor: pointer;"
                                ),method = "POST",
                                style="text-align: center; border: 1px none; background: #f5ebdc; padding: 8px;"
                            ),id = "result"
                                )
                                for coupon in coupon_list
                            ]
                        ),
                        style="""
                            background: #f5ebdc; 
                            border: 2px none;
                            width: 100%; 
                            margin: auto; 
                            text-align: center; 
                            position: relative; 
                            margin-top: 20px;
                        """
                    ),
                style="display: flex; flex-direction: column; background: #f5ebdc; padding: 20px; border-radius: 30px; width: 75%; height: 90vh; margin: auto; border: 1px solid #502314;"
                ),
            ),
            style="margin-top: 3%;background: #f5ebdc; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 20px;"
        )
    )

@rt('/use_coupon/{current_user_id}/{coupon_name}', methods=["GET", "POST"])
def use_coupon(current_user_id: int, coupon_name: str):
    user = system.search_user_by_id(current_user_id)

# Remove coupon from the user's list and deduct points
    if user.remove_coupon(coupon_name):
        # Assuming a coupon gives some discount, you can adjust the point deduction
        coupon = system.get_coupon_list().get(coupon_name)  # Find the coupon by name
        points_deducted = coupon.get_discount() * 10  # Example logic to convert discount to points
        user.add_point(-points_deducted)  # Deduct points

    return Div(Tbody(
        *[
            Tr(
                Td(coupon.get_name(), style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                Td(f"{coupon.get_discount()}%", style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                Td(coupon.get_expire_date(), style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                Td(
                    Button("Exchange",
                        hx_delete=f"/use_coupon/{current_user_id}/{coupon.get_name()}",
                        hx_target="#product-list",
                        hx_swap="outerHTML",
                        style="background: #D00; color: white; border: none; padding: 5px 10px; border-radius: 5px; cursor: pointer;"
                    ),
                    style="text-align: center; border: 1px solid #502314; background: #fff8f0; padding: 8px;"
                )
            ) for coupon in user.get_coupon()  # Loop through the user's coupons
        ]
    ), id="product-list")

serve()