from fasthtml.common import *

app, rt = fast_app(live=true)

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
            Div(
                H3("Payment", style="font-size: 36px;text-align: center; color: #502314;"),
                Form(
                    Group(
                        Div(
                            Label("ชื่อ",style="color: #502314; font-size: 18px; font-weight: bold;"),
                            Input(type="text", id="name", style="color: #000; background: #fff; padding: 8px; border-radius: 15px; border: 1px solid #502314;"),
                            style="display: flex; flex-direction: column; gap: 5px; width: auto; "
                        ),
                        Div(
                            Label("เบอร์โทรศัพท์มือถือ",style="color: #502314; font-size: 18px; font-weight: bold;"),
                            Input(type="text", id="No", style="color: #000; background: #fff;padding: 8px; border-radius: 15px; border: 1px solid #502314;"),
                            style="display: flex; flex-direction: column; gap: 5px; width: auto;"
                        ),
                        style="display: flex; gap: 15px; background: #fff; flex-direction: column; padding: 15px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);"
                    ),
                    H3("เลือกวิธีการชำระเงิน", style="font-size: 24px; color: #502314; margin-top: 20px;"),
                    Group(
                        Div(
                            Label("บัตรเครดิต/เดบิต", style="color: #502314; font-size: 18px; font-weight: bold;"),
                            Input(type="radio", id="credit", name="payment", value="credit", style="background:#fff; margin-left: 5px;"),
                            style="display: flex; flex-direction: column; gap: 5px; width: auto;"
                        ),
                        Div(
                            Label("QRCODE", style="color: #502314; font-size: 18px; font-weight: bold;"),
                            Input(type="radio", id="qrcode", name="payment", value="QRCODE", style="background:#fff; margin-left: 5px;"),
                            style="display: flex; flex-direction: column; gap: 5px; width: auto;"
                        ),
                        style="display: flex; flex-direction: column; gap: 15px; background: #fff; padding: 15px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);"
                    ),
                    Button("สั่งอาหาร", type="submit", style="background: #502314; color: white; font-weight: bold; padding: 10px 20px; border: none; border-radius: 20px; cursor: pointer; margin-top: 20px;"),
                    method="post",
                    action="/submit",
                    style="max-width: 500px; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);"
                )
            ),
            style="background: #f5ebdc; padding: 20px; min-height: 100vh; margin-top: 80px;"
        )
    )

@rt("/submit")
def post(name: str, No: str,payment:str):
    return f"ยืนยัน: {name},{No},{payment}"
serve()
