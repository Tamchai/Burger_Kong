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
            H1("Add new address", style="color: #502314; text-align: center; margin-top: 80px;"),
            Div(
                Div(
                    H4("Name address", style="color: #502314; margin-bottom: 5px; text-align: left;"),
                    Input(placeholder="Enter name address", 
                        style="color: #502314; width: 100%; background: #fff; padding: 10px; margin-bottom: 10px; border-radius: 10px; border: 1px solid #ddd;"),
                    H4("Address Detail", style="color: #502314; margin-bottom: 5px; text-align: left;"),
                    Input(id="address_input", placeholder="Enter address detail", 
                        style="color: #502314; width: 100%; background: #fff; padding: 10px; margin-bottom: 10px; border-radius: 10px; border: 1px solid #ddd;",
                        hx_on="input: document.getElementById('detail_address').innerText = this.value"),
                    Div(
                        P("Address", style="font-weight: bold; color: #502314; font-size: 20px; text-align: left; margin-bottom: 10px"),
                        P("", id="detail_address", 
                        style="text-align: left; color: #502314; background: #f5deb3; padding: 10px; border-radius: 10px; height: 100px"),
                    ),
                    Div(
                        Div(CheckboxX(checked=False), "Select as default",
                            style="font-weight: bold; color: #502314; font-size: 18px; display: flex; align-items: center; gap: 10px;"),
                        style="margin-top: 10px;"
                    ),
                    Button("Save", 
                        style="background: #D00000; color: white; padding: 10px 20px; border-radius: 10px;cursor: pointer; border: none; border-radius: 15px; font-size: 18px; margin-top: 15px; width: 100%;"
                    ),
                    style="background: #f5ebdc; padding: 20px; border-radius: 10px; width: 50%; margin: auto;box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2); border: 1px solid #ddd;"
                ),
                style="text-align: center; margin-top: 20px;"
            ),
            style="display: flex; flex-direction: column; align-items: center; min-height: 100vh; background: #f5ebdc; padding-bottom: 50px;"
        )
    )       

serve()