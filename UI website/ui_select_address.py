from fasthtml.common import *

app, rt = fast_app(live=True)

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
            H1("Select address", style="color: #502314; text-align: center; margin-top: 80px;"),
            Div(
                Div(
                    H3("name address", style="color: #502314; margin-bottom: 5px; text-align: left;"),
                    P("detail address", style="color: #502314; font-size: 16px; text-align: left;"),
                    Div(
                        Div(CheckboxX(checked=True), "Default",
                            style="font-weight: bold; color: #502314; font-size: 18px;"),
                        Button("Delete", 
                            style="font-size: 18px; text-decoration: underline; background: transparent; color: #D00000; font-weight: bold; border: none; cursor: pointer;"
                        ),
                        style="display: flex; align-items: center; gap: 10px; margin-top: 10px;"
                    ),
                    style="background: #fff; padding: 15px; border-radius: 10px; width: 50%; margin: auto;box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2); border: 1px solid #ddd;"
                ),
                style="text-align: center; margin-top: 20px;"
            ),
            Div(
                Button("Add new address", 
                    style="""display: flex; align-items: center; justify-content: center;
                             background: #fff; color: #D00000; padding: 10px 20px;
                             border-radius: 15px; margin-top: 20px; border: 1.5px solid #D00;
                             cursor: pointer;"""
                ),
                style="display: flex; justify-content: center; align-items: center; margin-top: 10px;"
            ),
            style="display: flex; flex-direction: column; align-items: center; min-height: 100vh; background: #f5ebdc; padding-bottom: 50px;"
        )
    )       

serve()
