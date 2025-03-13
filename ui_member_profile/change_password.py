from fasthtml.common import *
from dataclasses import dataclass

app, rt = fast_app(live=True)

@rt('/')
def get():
    return Container(
        Div(
            Div(
                Div(
                    Form(Button(
                        Img(src="https://i.imgur.com/fCpADUO.png", style="width: 50px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;",type="submit"),
                            action = "/home",method = "GET"
                    ),
                    H2("Burger Kong", style="color: #502314; margin: 0;"),
                    style="display: flex; align-items: center; gap: 10px;"
                ),
                Div(
                        Form(
                            Button(
                            Img(src="https://i.imgur.com/SwkvgTW.png",style="width: 40px; height: auto; margin-right: 15px;"),
                            style="background: none; border: none; cursor: pointer;", type = "submit"),),
                        Form(Button(
                        Img(src="https://i.imgur.com/Xyhfm0Q.png", style="width: 40px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;", type = "submit"), action = "####", method = "GET"),
                        Form(Button(
                            Img(src="https://i.imgur.com/JZR6dA6.png", style="width: 45px; height: auto;"),
                                style="background: none; border: none; cursor: pointer;", type = "submit"), ),
                        Form(Button(
                            Img(src="https://i.imgur.com/2eQjSEg.png", style="width: 45px; height: auto;"),
                                style="background: none; border: none; cursor: pointer;", type = "submit"),),
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
                H2("Change Password", style="color: #502314; font-size: 30px; font-weight: bold; margin-bottom: 20px;"),
                Div(
                    P("Your Password", style="color: #502314; text-align: left; font-size: 18px; font-weight: bold; margin-bottom: 3px;"),
                    Input(type="password", id="oldpassword", name="oldpassword", placeholder="Your Password", autocomplete="off",
                        style="color: #000; width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #502314; background: #fff;"),
                    P("New Password", style="color: #502314; text-align: left; font-size: 18px; font-weight: bold; margin-bottom: 3px;"),
                    Input(type="password", id="password", name="password", placeholder="New Password", autocomplete="off",
                        style="color: #000; width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #502314; background: #fff;"),
                    P("Confirm Password", style="color: #502314; text-align: left; font-size: 18px; font-weight: bold; margin-bottom: 3px;"),
                    Input(type="password", id="confirm_password", name="confirm_password", placeholder="Confirm Password", autocomplete="off",
                        style="color: #000; width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #502314; background: #fff;"),
                    Button("Update Password", type="submit", id="update-password-btn",
                        style="background: #d32f2f; color: white; padding: 12px; border: none; border-radius: 20px; cursor: pointer; width: 100%; font-weight: bold; font-size: 18px; margin-top: 10px;"),
                style="""
                        background: #f5ebdc;
                        padding: 30px;
                        border-radius: 10px;
                        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3);
                        text-align: center;
                        max-width: 600px;
                        margin: auto;
                        border: 2px solid #502314;
                        min-height: auto;
                    """
                ),
            style="position: relative; margin-top: 2%; display: flex; flex-direction: column; align-items: center;"
            ),
        style="background: #f5ebdc; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0;"
        )
    )
serve()