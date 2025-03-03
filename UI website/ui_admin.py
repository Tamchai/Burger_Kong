from fasthtml.common import *
from dataclasses import dataclass

app, rt = fast_app(live=True)
products = []

@dataclass
class Product:
   name: str; price: float; description: str

@rt('/')
def get():
    return Container(
         Div(
            Div(
                 Img(src="https://i.imgur.com/fCpADUO.png", 
                    style="width: 70px; height: auto; margin: 0px;"),
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
               H2("Product Manager",style="color: #502314; text-align: center;"),
               Input(id="name",name="name",placeholder="Name",
                        style="color: #000; background: #fff; border-radius: 5px; border: 2px solid #502314;"),
               Input(id="price",name="price",type="number",step="0.01",
                        style="color: #000; background: #fff; border-radius: 5px; border: 2px solid #502314;"), 
               Input(id="description",name="description",placeholder="Description",
                        style="color: #000; background: #fff; border-radius: 5px; border: 2px solid #502314;"), 
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
                     Th("Name", style="text-align: center; background: #502314; color: #fff; padding: 10px; border: 1px solid #502314;"),
                     Th("Price", style="text-align: center; background: #502314; color: #fff; padding: 10px; border: 1px solid #502314;"),
                     Th("Description", style="text-align: center; background: #502314; color: #fff; padding: 10px; border: 1px solid #502314;"),
                     Th("Action", style="text-align: center; background: #502314; color: #fff; padding: 10px; border: 1px solid #502314;"),
                  )
               ),
               Tbody(
                  *[
                     Tr(
                        Td(p.name, style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                        Td(f"${p.price:,.2f}", style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                        Td(p.description, style="color:#502314; background: #fff8f0; padding: 8px; border: 1px solid #502314;"),
                        Td(
                           Button("Delete",
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
        style="background: #f5ebdc; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 20px;"
        )
    )

@rt("/product")
def post(product: Product):
   products.append(product)
   return RedirectResponse("/", status_code=303)

serve()