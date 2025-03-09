from fasthtml.common import *
from dataclasses import dataclass

app, rt = fast_app(live=True)
products = []

class Product:
    def __init__(self,name,percent,expiration):
        self.name = name
        self.percent = percent  
        self.expiration = expiration

@rt('/')
def get():
    return Container(
         Div(
            Div(
                Button(
                    Img(src="https://i.imgur.com/fCpADUO.png", style="width: 60px; height: auto;"),
                        style="background: none; border: none; cursor: pointer;"),
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
                Input(id="name",name="name",placeholder="Name menu",
                        style="color: #000; background: #fff; border-radius: 5px; border: 2px solid #502314;"),
               ),
               Div(
                P("Percent",style="font-size: 18px; font-weight: bold; color: #502314; text-align: left; margin-bottom: 2px;"),
                Input(id="percent",name="percent",type="number",step="1",
                        style="color: #000; background: #fff; border-radius: 5px; border: 2px solid #502314;"), 
               ),
               Div(
                P("Expiration date",style="font-size: 18px; font-weight: bold; color: #502314; text-align: left; margin-bottom: 2px;"),
                Input(id="expiration",name="expiration",placeholder="Expiration date",
                        style="color: #000; background: #fff; border-radius: 5px; border: 2px solid #502314;"), 
               ),
               Button("Add",style="font-weight: bold; font-size: 16px; color: #fff; text-align: center; background: #502314; border-radius: 5px; border: none; width: 90px;"),
               method="post",
               action="/product",
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
                     Th("Name Coupone", style="text-align: center; background: #502314; color: #fff; padding: 10px; border: 1px solid #502314;"),
                     Th("Percent", style="text-align: center; background: #502314; color: #fff; padding: 10px; border: 1px solid #502314;"),
                     Th("Expiration Date", style="text-align: center; background: #502314; color: #fff; padding: 10px; border: 1px solid #502314;"),
                     Th("Action", style="text-align: center; background: #502314; color: #fff; padding: 10px; border: 1px solid #502314;"),
                  )
               ),
               Tbody(
                  *[
                     Tr(
                        Td(p.name, style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                        Td(f"{p.percent}%", style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                        Td(p.expiration, style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                        Td(
                           Button("Delete",
                            hx_post=f"/delete/{p.name}",
                            hx_target="#product",
                            hx_swap="outerHTML",
                            style="background: #D00; color: white; border: none; padding: 5px 10px; border-radius: 5px; cursor: pointer;"
                        ),
                           style="text-align: center; border: 1px solid #502314; background: #fff8f0; padding: 8px;"
                        )
                     ) 
                     for p in products
                  ]
               ),
               style="""
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
        style="margin-top: 3%;background: #f5ebdc; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 20px;"
        )
    )

@rt("/product")
def post(name:str,percent:int,expiration:str):
    global products
    product = Product(name,percent,expiration)
    products.append(product)
    return RedirectResponse("/", status_code=303)

@rt("/delete/{name}")
def delete(name: str):
    global products
    products = [p for p in products if p.name != name]
    return RedirectResponse("/", status_code=303)

serve()
