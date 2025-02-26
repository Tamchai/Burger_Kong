from fasthtml.common import *

app, rt = fast_app(live=True)

user_points = 150

coupons = [
    {"id": 1, "name": "ส่วนลด 10%", "points": 100},
    {"id": 2, "name": "ฟรีเฟรนช์ฟรายส์", "points": 200}
]

@rt('/')
def get():
    return Container(
        Div(
            Div(
                Div(
                    Button("☰", 
                        style="""
                            background: transparent; 
                            border: none; 
                            color: #502314;
                            font-size: 24px;
                            width: 40px; 
                            height: 40px;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            margin: 0;
                            padding: 0;
                            cursor: pointer;
                        """
                    ),
                    Img(src="https://i.imgur.com/fCpADUO.png", 
                        style="width: 55px; height: auto; margin: 0px;"
                    ),
                    H2("Burger Kong", style="color: #502314; margin: 0;"),
                    style="display: flex; align-items: center; gap: 10px;"
                ),
                Div(
                    Img(src="https://i.imgur.com/Xyhfm0Q.png",
                        style="width: 40px; height: auto; margin-right: 15px;"),
                    Img(src="https://i.imgur.com/AcIDazc.png",
                        style="width: 40px; height: auto; margin-right: 15px;"),
                    Img(src="https://i.imgur.com/Kj7efMN.png",
                        style="width: 40px; height: auto; margin-right: 10px;"),
                    Img(src="https://i.imgur.com/2eQjSEg.png",
                        style="width: 40px; height: auto; margin-right: 20px;"),
                    style="color: #502314; font-size: 20px; font-weight: bold; display: flex; justify-content: flex-end; align-items: center;"
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
                        Button("เพิ่มคูปอง", id="add-coupon", hx_post="/add-coupon", hx_target="#cart-items", style="background: #502314; color: white; padding: 5px 10px; border: none; border-radius: 10px; cursor: pointer;"),
                        style="display: flex; justify-content: space-between; align-items: center; width: 100%; padding-bottom: 10px;"
                    ),
                    Div(id="cart-items", children=[generate_coupon_list()], style="flex-grow: 1; width: 100%;"),
                    style="display: flex; flex-direction: column; width: 100%; height: 100%; flex-grow: 1;"
                ),
                style="display: flex; flex-direction: column; background: #f5ebdc; padding: 20px; border-radius: 30px; width: 75%; height: 90vh; margin: auto; border: 1px solid #502314;"
            ),
            style="background: #f5ebdc; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 20px;"
        )
    )

# ฟังก์ชันสร้างรายการคูปอง
def generate_coupon_list():
    return Div(
        *[
            Div(
                P(f"{coupon['name']} - ใช้ {coupon['points']} แต้ม", style="color: #502314; padding: 5px 0;"),
                Button("แลก", style="background: #502314; color: white; padding: 5px 10px; border: none; border-radius: 10px; cursor: pointer;"),
                style="display: flex; justify-content: space-between; align-items: center; padding: 10px; border-bottom: 1px solid #502314;"
            )
            for coupon in coupons
        ]
    )

# API สำหรับเพิ่มคูปองใหม่ (Admin เท่านั้น)
@rt('/add-coupon', methods=["POST"])
def add_coupon():
    new_coupon = {"id": len(coupons) + 1, "name": "ส่วนลด 20%", "points": 300}
    coupons.append(new_coupon)
    return generate_coupon_list()

serve()