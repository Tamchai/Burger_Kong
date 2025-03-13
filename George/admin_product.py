from fasthtml.common import *
from routing import app, rt
import server
from server import Menu
from server import MenuSet
from server import Burger
from server import Beverage
import admin 
from win10toast import ToastNotifier
system = server.system 
product_list = system.get_menu_list()
n = ToastNotifier()

@rt('/product_manager', methods=["GET","POST"])
def product_manager():
    global product_list
    return Title("Admin page"), Container(
        Div(
            Div(
                Button(
                    Img(src="https://i.imgur.com/fCpADUO.png", style="width: 60px; height: auto;"),
                    style="background: none; border: none; cursor: pointer;",
                    type="button",
                    onclick="history.back()"
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
                H2("Product Manager", style="color: #502314; text-align: center;"),
                Div(
                    P("Image URL", style="font-size: 18px; font-weight: bold; color: #502314; text-align: left; margin-bottom: 2px;"),
                    Input(id="image_url", name="image_url", type="text", placeholder="Enter Image URL",
                          style="color: #502314; background: #fff; border-radius: 5px; border: 2px solid #502314;"),
                ),
                Div(
                    P("Name Menu", style="font-size: 18px; font-weight: bold; color: #502314; text-align: left; margin-bottom: 2px;"),
                    Input(id="name", name="name", placeholder="Name menu",
                          style="color: #000; background: #fff; border-radius: 5px; border: 2px solid #502314;"),
                ),
                Div(
                    P("Price", style="font-size: 18px; font-weight: bold; color: #502314; text-align: left; margin-bottom: 2px;"),
                    Input(id="price", name="price", type="number", step="0.01",
                          style="color: #000; background: #fff; border-radius: 5px; border: 2px solid #502314;"),
                ),
                Div(
                    P("Description", style="font-size: 18px; font-weight: bold; color: #502314; text-align: left; margin-bottom: 2px;"),
                    Input(id="description", name="description", placeholder="Description",
                          style="color: #000; background: #fff; border-radius: 5px; border: 2px solid #502314;"),
                ),
                Div(
                    P("Category", style="font-size: 18px; font-weight: bold; color: #502314; text-align: left; margin-bottom: 2px;"),
                    Select(
                        Option("Burger", value="Burger"),
                        Option("Snack", value="Snack"),
                        Option("Beverage", value="Beverage"),
                        Option("Menu Set", value="Menu Set"),
                        style="color: #000; background: #fff; border-radius: 5px; border: 2px solid #502314;",
                        id="category", name="category", placeholder="Category"
                    ),
                ),
                Button("Add", style="font-weight: bold; font-size: 16px; color: #fff; text-align: center; background: #502314; border-radius: 5px; border: none; width: 90px;"),
                method="POST",
                action="/add_product",
                style="""
                  background: #f5ebdc; 
                  padding: 15px; 
                  border-radius: 10px; 
                  width: 90%; 
                  border: 1px solid #502314; 
                  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3);
                  margin: auto;
                  position: relative;
                  top: -50px;
                """
            ),
            Table(
                Thead(
                    Tr(
                        Th("Image", style="text-align: center; background: #502314; color: #fff; padding: 10px; border: 1px solid #502314;"),
                        Th("Name", style="text-align: center; background: #502314; color: #fff; padding: 10px; border: 1px solid #502314;"),
                        Th("Price", style="text-align: center; background: #502314; color: #fff; padding: 10px; border: 1px solid #502314;"),
                        Th("Description", style="text-align: center; background: #502314; color: #fff; padding: 10px; border: 1px solid #502314;"),
                        Th("Category", style="text-align: center; background: #502314; color: #fff; padding: 10px; border: 1px solid #502314;"),
                        Th("Action", style="text-align: center; background: #502314; color: #fff; padding: 10px; border: 1px solid #502314;"),
                    )
                ),
                # กำหนด id ให้กับ tbody เพื่อให้ hx_target ใช้ได้ถูกต้อง
                Tbody(
                    *[
                        Tr(
                            Td(
                                Img(src=p.get_src(), style="width: 50px; height: auto;"),
                                style="text-align: center; background: #fff8f0; padding: 8px; border: 1px solid #502314;"
                            ),
                            Td(p.get_name(), style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                            Td(f"${p.get_price():,.2f}", style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                            Td(p.get_details(), style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                            Td(p.get_category(), style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                            Td(
                                Button("Delete",
                                    hx_delete=f"/delete_product/{p.get_name()}",
                                    hx_target="#product-table",  # กำหนดให้ target เป็น tbody ที่มี id product-table
                                    hx_swap="outerHTML",
                                    style="background: #D00; color: white; border: none; padding: 5px 10px; border-radius: 5px; cursor: pointer;"
                                ),
                                style="text-align: center; border: 1px solid #502314; background: #fff8f0; padding: 8px;"
                            )
                        )
                        for p in product_list
                    ],
                    id="product-table"
                ),
                style="""
                  margin-top: 3%;
                  background: #f5ebdc;
                  border: 2px solid #502314;
                  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3);
                  width: 90%;
                  margin: auto;
                  border-radius: 10px;
                  text-align: center;
                  position: relative;
                  top: -35px;
                """
            ),
            style="margin-top: 7%;background: #f5ebdc; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 20px;"
        )
    )

@app.post("/add_product")
def add_coupon(image_url:str, name:str, price:int, description:str, category:str):
    global product_list
    if category == "Burger":
        product_to_add = server.Burger("Burger",len(server.system.get_menu_list())+1,name,price,description,image_url)
        system.add_menu(product_to_add)
        return RedirectResponse("/product_manager")
    elif category == "Beverage":
        product_to_add = server.Beverage("Beverage",len(server.system.get_menu_list())+1,name,price,description,image_url)
        system.add_menu(product_to_add)
        return RedirectResponse("/product_manager")
    elif category == "Snack":
         product_to_add = server.Snack("Snack",len(server.system.get_menu_list())+1,name,price,description,image_url)
         system.add_menu(product_to_add)
         return RedirectResponse("/product_manager")
    else :
        return n.show_toast("Wrong", "Category not found", duration = 10, icon_path ="/picture/logo.ico")

@rt("/delete_product/{name}", methods=["DELETE"])
def delete_product(name: str):
    global product_list
    product_list = [p for p in product_list if p.get_name() != name]
    # ส่งกลับ tbody ที่อัปเดตแล้วให้กับ htmx
    return Div(
        Tbody(
            *[
                Tr(
                    Td(
                        Img(src=p.get_src(), style="width: 50px; height: auto;"),
                        style="text-align: center; background: #fff8f0; padding: 8px; border: 1px solid #502314;"
                    ),
                    Td(p.get_name(), style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                    Td(f"${p.get_price():,.2f}", style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                    Td(p.get_details(), style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                    Td(p.get_category(), style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                    Td(
                        Button("Delete",
                            hx_delete=f"/delete_product/{p.get_name()}",
                            hx_target="#product-table",
                            hx_swap="outerHTML",
                            style="background: #D00; color: white; border: none; padding: 5px 10px; border-radius: 5px; cursor: pointer;"
                        ),
                        style="text-align: center; border: 1px solid #502314; background: #fff8f0; padding: 8px;"
                    )
                )
                for p in product_list
            ]
        ),
        id="product-table"
    )
@rt("/delete_product/{name}", methods=["DELETE"])
def delete_product(name: str):
    global product_list
    product_list = [p for p in product_list if p.get_name() != name]
    response = Response(status_code=200)
    response.headers["HX-Redirect"] = "/product_manager"
    return response
serve()