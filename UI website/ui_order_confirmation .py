from fasthtml.common import *

app, rt = fast_app(live=True)

@rt('/')
def get():
    return Container(
        Div(
            Div(
                Div(
                    Button("☰", 
                        style="""background: transparent; border: none; color: #502314;
                                 font-size: 24px; width: 40px; height: 40px; display: flex;
                                 align-items: center; justify-content: center; margin: 0;
                                 padding: 0; cursor: pointer;"""
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
            style="""width: 100%; background: #f5ebdc; padding: 15px; border-bottom: 2px solid #502314;
                     position: fixed; top: 0; left: 0; width: 100%; z-index: 1000;
                     box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.5);"""
        ),
        Body(
            H1("Order Confirmation", style="color: #502314; text-align: center; margin-top: 80px;"),
            Div(
                P("BURGERKONG", style="color: #502314; font-size: 36px; text-align: center; font-weight: bold;"),
                P("Order Number: #123456", style="color: #502314; font-size: 18px; text-align: center; font-weight: bold;"),
                #รอเอาข้อมูลมาใส่
                P("Address", style="color: #502314; font-size: 18px; text-align: left; font-weight: bold;"),
                Div(
                Table(
                        Tr(
                            Th("Name", style="font-size: 20px; font-weight: bold; text-align: left; background: #fff; color: #000; padding: 1px; border-bottom: 2px solid rgba(0, 0, 0, 0.5);"),
                            Th("Price", style="font-size: 20px; font-weight: bold;text-align: left; background: #fff; color: #000; padding: 1px; border-bottom: 2px solid rgba(0, 0, 0, 0.5);"),
                            Th("Amount", style="font-size: 20px; font-weight: bold;text-align: left; background: #fff; color: #000; padding: 1px; border-bottom: 2px solid rgba(0, 0, 0, 0.5); "),
                        ),
                        *[
                            Tr(
                                Td(item["name"], style="font-size: 16px; text-align: left; color: #000; background: #fff; padding: 1px; border: none;"),
                                Td(f"${item['price']}", style="font-size: 16px; text-align: left; color: #000; background: #fff; padding: 1px; border: none;"),
                                Td(str(item["amount"]), style="font-size: 16px; text-align: left; color: #000; background: #fff; padding: 1px; border: none;"),
                            )
                            #อันนี้แค่สมมุติค่าไว้เฉยๆ
                            for item in [
                                {"name": "Burger", "price": 5.99, "amount": 2},
                                {"name": "Fries", "price": 2.49, "amount": 1},
                                {"name": "Soda", "price": 1.99, "amount": 1},
                            ]
                        ],
                        style="width: 100%; border-collapse: collapse;"
                    ),
                ),
                Hr(style="border: 1px solid #000; opacity: 0.5;"),
                Div(
                    P("Total", style="color: #502314; font-size: 26px; font-weight: bold; display: table-cell; text-align: left;"),
                    #ใส่ยิดเงินรวมทั้งหมด
                    P("0.00 $", style="color: #502314; font-size: 26px; font-weight: bold; display: table-cell; text-align: right;"),
                    style="display: table; width: 100%;"
                ),
                Hr(style="border: 1px solid #000; opacity: 0.5;"),
                Div(
                    #ใส่ช่องทางการจ่ายเงิน
                    P("Payment", style="color: #502314; font-size: 24px; font-weight: bold; display: table-cell; text-align: left;"),
                    P("0.00 $", style="color: #502314; font-size: 26px; font-weight: bold; display: table-cell; text-align: right;"),
                    style="display: table; width: 100%;"
                ),
                Hr(style="border: 1px solid #000; opacity: 0.5;"),
                Button("Back to Home",
                    style="font-weight: bold; background: #D00000; color: white; padding: 10px 20px; border-radius: 15px; cursor: pointer; border: none; font-size: 18px; margin-top: 40px; width: 100%;"
                ),
                style="background: #fff; padding: 20px; border-radius: 10px; width: 50%; margin: auto; text-align: center; box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2); border: 1px solid #ddd;"
            ),
            style="display: flex; flex-direction: column; align-items: center; min-height: 100vh; background: #f5ebdc; padding-bottom: 50px;"
        )
    )        

serve()