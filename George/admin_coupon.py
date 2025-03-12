from fasthtml.common import *
from routing import app, rt
import server
import admin
from win10toast import ToastNotifier
system = server.system 
# product =system.get_coupon_list()
# app, rt = fast_app(live=True)
coupon_list = system.get_coupon_list()
# import win10toast


# create an object to ToastNotifier class
n = ToastNotifier()



@rt('/coupon_manager', methods=["GET","POST"])
def coupon_manager():
    return Container(
         Div(
            Div(
                Button(
                    Img(src="https://i.imgur.com/fCpADUO.png", style="width: 60px; height: auto;"),
                        style="background: none; border: none; cursor: pointer;",
                        type = "button",
                        onclick = "history.back()"
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
                width: 100%; 
                z-index: 1000;
                box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.5);
                text-align: center;
            """
         ),
        Body(
            Form(
               H2("Coupon Manager",style="color: #502314; text-align: center;"),
               Div(
                P("Name Coupon",style="font-size: 18px; font-weight: bold; color: #502314; text-align: left; margin-bottom: 2px;"),
                Input(id="name",name="name",placeholder="Name menu", required=True,
                        style="color: #000; background: #fff; border-radius: 5px; border: 2px solid #502314;"),
               style="margin-bottom: 15px;"
               ),
               Div(
                P("Percent",style="font-size: 18px; font-weight: bold; color: #502314; text-align: left; margin-bottom: 2px;"),
                Input(id="percent",name="percent",type="number",step="1", required=True,
                        style="color: #000; background: #fff; border-radius: 5px; border: 2px solid #502314;"), 
               style="margin-bottom: 15px;"
               ),
               Div(
                P("Expiration date",style="font-size: 18px; font-weight: bold; color: #502314; text-align: left; margin-bottom: 2px;"),
                Input(id="expiration",type = "date",name="expiration",placeholder="Expiration date", required=True,
                        style="color: #000; background: #fff; border-radius: 5px; border: 2px solid #502314;"), 
               style="margin-bottom: 15px;"
               ),
               Button("Add",style="font-weight: bold; font-size: 16px; color: #fff; text-align: center; background: #502314; border-radius: 5px; border: none; width: 90px;"),
               method="POST",
               action="/add_coupon",
               style="""
                  background: #f5ebdc; 
                  padding: 20px; 
                  border-radius: 10px; 
                  width: 90%;
                  min-width: 320px; 
                  border: 1px solid #502314; 
                  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3);
                  margin: auto;
                  position: relative;
                  top: -50;
                """
            ),
            Table(
               Thead(
                  Tr(
                     Th("Name Coupone", style="text-align: center; background: #502314; color: #fff; padding: 10px; border: 1px solid #502314;"),
                     Th("Percent", style="text-align: center; background: #502314; color: #fff; padding: 10px; border: 1px solid #502314;"),
                     Th("Expiration Date", style="text-align: center; background: #502314; color: #fff; padding: 10px; border: 1px solid #502314;"),
                     Th("Action", style="text-align: center; background: #502314; color: #fff; padding: 10px; border: 1px solid #502314;"),
                  )
               ),
               Tbody(
                    # hx_preserve="true",
                    id="product-list",# Add this ID for targeting updates
                    *[
                        Tr(
                            Td(p.get_name(), style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                            Td(f"{p.get_discount()}%", style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                            Td(p.get_expire_date(), style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                            Td(
                                Button("Delete",
                                    hx_delete=f"/delete/{p.get_name()}",  # ✅ Use hx_delete for proper HTTP semantics
                                    hx_target=f"#{p.get_name()}",  # ✅ Targets the table body
                                    hx_swap="outerHTML",  # ✅ Replaces only the table body, not the full page
                                    style="background: #D00; color: white; border: none; padding: 5px 10px; border-radius: 5px; cursor: pointer;"
                                ),
                                style="text-align: center; border: 1px solid #502314; background: #fff8f0; padding: 8px;"
                            ),id = p.get_name()
                        )
                        for p in coupon_list
                    ]
                ),
               style="""
                    background: #f5ebdc; border: 2px solid #502314;
                    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3);
                    width: 90%; margin: auto; border-radius: 10px;
                    text-align: center; position: relative; margin-top: 20px;
               """
            ),
            style="""
                margin-top: 120px; background: #f5ebdc; min-height: 100vh;
                display: flex; flex-direction: column; align-items: center; 
                justify-content: flex-start; padding: 20px;
            """
        )
    )

@app.post("/add_coupon")
def add_coupon(name:str,percent:int,expiration:str):
    global coupon_list
    if not coupon_list:
        coupon_to_add = server.Coupon(name,percent,expiration)
        coupon_list.append(coupon_to_add)
        return RedirectResponse("/coupon_manager")
    else :
        for coupon in coupon_list:
            if coupon.get_name() == name or percent > 100 :
                return n.show_toast("Wrong", "Coupon name already exist", duration = 10, icon_path ="/picture/logo.ico")
            else :
                coupon_to_add = server.Coupon(name,percent,expiration)
                coupon_list.append(coupon_to_add)
                return RedirectResponse("/coupon_manager")

@rt("/delete/{name}")
def delete(name: str):
    global coupon_list
    coupon_list = [p for p in coupon_list if p.get_name() != name]
    return Div(Tbody(
        *[
            Tr(
                Td(p.get_name(), style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                Td(f"{p.get_discount()}%", style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                Td(p.get_expire_date(), style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                Td(
                    Button("Delete",
                        hx_delete=f"/delete/{p.get_name()}",
                        hx_target="#product-list",  # Updated target to the container of the coupon list
                        hx_swap="outerHTML",
                        style="background: #D00; color: white; border: none; padding: 5px 10px; border-radius: 5px; cursor: pointer;"
                    ),
                    style="text-align: center; border: 1px solid #502314; background: #fff8f0; padding: 8px;"
                )
            ) for p in coupon_list
        ]
    ), id="product-list")



serve()
