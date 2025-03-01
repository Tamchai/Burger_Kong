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
                Div(
                    Button("<", 
                        type="button", 
                        style="""
                            position: absolute; 
                            top: 100px; 
                            left: 20px; 
                            background: none; 
                            border: none; 
                            color: #502314; 
                            font-size: 22px; 
                            font-weight: bold; 
                            cursor: pointer;
                        """
                    )
                ),
                Form(
                    H3("Welcome to BURGERKONG", style="font-size: 24px; text-align: center; color: #502314; font-weight: bold; font-family: 'Arial', sans-serif;"),
                    Div(
                        Input(type="text", name="username", placeholder="User",
                              style="color: #000; width: 80%; padding: 10px; margin: 10px 0; border-radius: 15px; border: 2px solid #502314; background: #fff;"),
                    ),
                    Div(
                        Input(type="password", name="password", placeholder="Password", autocomplete="off",
                              style="color: #000; width: 80%; padding: 10px; margin: 10px 0; border-radius: 15px; border: 2px solid #502314; background: #fff;"),
                    ),
                    Div(
                        Button("Sign In", type="submit", style="background: #b22222; color: white; padding: 12px; border: none; border-radius: 20px; cursor: pointer; width: 85%; margin-top: 10px; font-weight: bold;"),
                        method="post",
                        action="/login",
                    ),
                    Div("Don't Have An Account?", style="margin-top: 10px; margin-bottom: 2px; font-size: 16px; color: #502314;"),
                    Div(
                        Button("Create Account", href="/register", style="background: #b22222; color: white; padding: 12px; border: none; border-radius: 20px; cursor: pointer; width: 85%; margin-top: 10px; font-weight: bold;"),
                        method="post",
                        action="/register",
                    ),
                    style="""
                        background: #f5ebdc; 
                        padding: 30px; 
                        border-radius: 10px; 
                        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3); 
                        text-align: center; 
                        max-width: 400px; 
                        margin: auto; 
                        border: 2px solid #502314;
                        position: relative;
                        top: -70px;
                    """
                )
            ),
            style="background: #f5ebdc; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0;"
        )
    )

serve()
