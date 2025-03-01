from fasthtml.common import *

app, rt = fast_app(live=true)

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
            
            Div(
                H3("Create Account", 
                   style="font-size: 32px; text-align: center; color: #502314; font-weight: bold; font-family: 'Arial', sans-serif; margin-top: 50px;"),
                Button("<", 
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
                        Label(Input(type="radio", name="title", value="mr"), " Mr.",
                            style="color: #502314; font-size: 18px; font-weight: bold;"),
                        Label(Input(type="radio", name="title", value="ms"), " Ms.",
                            style="color: #502314; font-size: 18px; font-weight: bold;"),
                        Label(Input(type="radio", name="title", value="mrs"), " Mrs.",
                            style="color: #502314; font-size: 18px; font-weight: bold;"),
                        style="display: flex; gap: 10px; margin-bottom: 15px; align-items: center;"
                    ),
                    Div(
                        Input(type="text", name="firstname", placeholder="*Firstname", required=True,
                            style="color: #000; width: 47%; padding: 10px; border-radius: 5px; border: 1px solid #502314; background: #fff;"),
                        Input(type="text", name="lastname", placeholder="*Lastname", required=True,
                            style="color: #000; width: 47%; padding: 10px; border-radius: 5px; border: 1px solid #502314; background: #fff;"),
                        style="display: flex; justify-content: space-between; margin-bottom: 10px;"
                    ),
                    Div(
                        Input(type="text", name="mobile", placeholder="*Mobile no.", required=True,
                            style="color: #000; width: 47%; padding: 10px; border-radius: 5px; border: 1px solid #502314; background: #fff;"),
                        Input(type="date", name="birthdate", placeholder="*Birth Day", required=True,
                            style="color: #000; width: 47%; padding: 10px; border-radius: 5px; border: 1px solid #502314; background: #fff;"),
                        style="display: flex; justify-content: space-between; margin-bottom: 10px;"
                    ),
                    Div(
                        Input(type="email", name="email", placeholder="*Email", required=True,
                            style="color: #000; width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #502314; background: #fff;"),
                        style="margin-bottom: 10px;"
                    ),
                    Div(
                        Input(type="checkbox", name="confirm", required=True),
                        " Confirm Register",
                        style="color: #502314; margin-bottom: 15px; text-align: left; font-size: 16px; font-weight: bold;"
                    ),
                    Button("Register", type="submit",
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
                        """
                    ),
                    method="post",
                    action="/register",
                    style="""
                        background: #f5ebdc;
                        padding: 30px;
                        border-radius: 10px;
                        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3);
                        text-align: center;
                        max-width: 450px;
                        margin: auto;
                        border: 2px solid #502314;
                    """
                ),
                style="position: relative; top: -100px;"
            ),
            style="background: #f5ebdc; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0;"
        )
    )

serve()
