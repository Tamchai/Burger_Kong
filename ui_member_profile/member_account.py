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
                H3("Your Account", 
                style="font-size: 32px; text-align: center; color: #502314; font-weight: bold; font-family: 'Arial', sans-serif;"),
                Button("<", 
                        type = "button" , onclick = "history.back()",
                        style="""
                            position: fixed; 
                            top: 100px; 
                            left: 15px; 
                            background: none; 
                            border: none; 
                            color: #502314; 
                            font-size: 24px; 
                            font-weight: bold; 
                            cursor: pointer;
                            z-index: 1100;
                        """
                    ),
                Form(
                    Div(
                        Div(
                            Label(Input(type="radio", id="title-mr", name="title", value="mr", required=True), " Mr.",
                                style="color: #502314; font-size: 18px; font-weight: bold;"),
                            Label(Input(type="radio", id="title-ms", name="title", value="ms", required=True), " Ms.",
                                style="color: #502314; font-size: 18px; font-weight: bold;"),
                            Label(Input(type="radio", id="title-mrs", name="title", value="mrs", required=True), " Mrs.",
                                style="color: #502314; font-size: 18px; font-weight: bold;"),
                            style="display: flex; gap: 15px;"
                        ),
                        style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 15px;"
                    ),
                    Div(
                        Input(type="text", id="firstname", name="firstname", placeholder="*Firstname", required=True,
                            style="color: #000; width: 70%; padding: 10px; border-radius: 5px; border: 1px solid #502314; background: #fff;"),
                        Input(type="text", id="lastname", name="lastname", placeholder="*Lastname", required=True,
                            style="color: #000; width: 70%; padding: 10px; border-radius: 5px; border: 1px solid #502314; background: #fff;"),
                        style="display: flex; justify-content: space-between; margin-bottom: 5px; gap: 10px;"
                    ),
                    Div(
                        Input(type="text", id="mobile", name="mobile", placeholder="*Mobile no.", required=True,
                            style="color: #000; width: 70%; padding: 10px; border-radius: 5px; border: 1px solid #502314; background: #fff;"),
                        Input(type="date", id="birthdate", name="birthdate", placeholder="*Birth Day", required=True,
                            style="color: #000; width: 70%; padding: 10px; border-radius: 5px; border: 1px solid #502314; background: #fff;"),
                        style="display: flex; justify-content: space-between; margin-bottom: 5px; gap: 10px;"
                    ),
                    Div(
                        Input(type="email", id="email", name="email", placeholder="*Email", required=True,
                              style="color: #000; width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #502314; background: #fff;"),
                        style="margin-bottom: 1px;"
                    ),
                    Div(
                        P("Password", style="color: #502314; text-align: left; font-size: 18px; font-weight: bold; margin-bottom: 3px;"),
                        Button("Change Password", type="button", id="toggle-password-btn", 
                            style="background: none; color: #D00; text-decoration: underline; padding: 12px; border: none; border-radius: 20px; cursor: pointer; font-weight: bold; font-size: 16px;"),
                        style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 5px;"
                    ),
                    Button("Your Order", type="submit",
                        id="Order button",
                        style="""
                            background: #502314;
                            color: white;
                            padding: 12px;
                            border: none;
                            border-radius: 20px;
                            cursor: pointer;
                            width: 100%;
                            font-weight: bold;
                            font-size: 18px;
                            margin-top: 10px;
                        """
                    ),
                    Button("Logout", type="submit",
                        id="logout button",
                        style="""
                            background: #d32f2f;
                            color: white;
                            padding: 12px;
                            border: none;
                            border-radius: 20px;
                            cursor: pointer;
                            width: 100%;
                            font-weight: bold;
                            font-size: 18px;
                            margin-top: 10px;
                        """
                    ),
                    style="""
                        background: #f5ebdc;
                        padding: 30px;
                        border-radius: 10px;
                        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3);
                        text-align: center;
                        max-width: 600px;
                        margin: auto;
                        border: 2px solid #502314;
                        min-height: 500px;
                    """
                ),
                style="position: relative; margin-top: 2%; display: flex; flex-direction: column; align-items: center;"
            ),
            style="background: #f5ebdc; display: flex; justify-content: center; align-items: center; min-height: 120vh; margin: 0;"
        )
    )

serve()