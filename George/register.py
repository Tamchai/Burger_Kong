from fasthtml.common import *
from routing import app, rt
import server
from server import Admin 
# app, rt = fast_app(live=True)
system = server.system  

@app.get('/')
def login_page():
    return Title("Burger Kong"),Container(
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
                Form(
                        H3("Welcome to BURGERKONG", style="font-size: 24px; text-align: center; color: #502314; font-weight: bold; font-family: 'Arial', sans-serif;"),
                        Div(
                            Input(type="text",id = "username", name="username", placeholder="Username", required=True,
                                style="color: #000; width: 80%; padding: 10px; margin: 10px 0; border-radius: 15px; border: 2px solid #502314; background: #fff;"),
                        ),
                        Div(
                            Input(type="password",id = "password", name="password", placeholder="Password", autocomplete="off", required=True,
                                style="color: #000; width: 80%; padding: 10px; margin: 10px 0; border-radius: 15px; border: 2px solid #502314; background: #fff;"),
                        ),
                        
                            Button("Sign In", type="submit", style="background: #b22222; color: white; padding: 12px; border: none; border-radius: 20px; cursor: pointer; width: 85%; margin-top: 10px; font-weight: bold;"),
                            method="GET",
                            action="/login",
                        
                    ),
                    Div("Don't Have An Account?", style="margin-top: 10px; margin-bottom: 2px; font-size: 16px; color: #502314;"),
                Div(
                        Form(
                            Button("Create Account", type = "submit",style="background: #b22222; color: white; padding: 12px; border: none; border-radius: 20px; cursor: pointer; width: 85%; margin-top: 10px; font-weight: bold;")
                            ,action="/register",
                            method = "GET"
                        )             
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
            ),
            style="background: #f5ebdc; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0;"
        )
    )

@app.get('/register')
def creat_account_page():
    return Title("Burger Kong"), Container(
        Div(
            Div(
                Div(
                    Img(src="https://i.imgur.com/fCpADUO.png", 
                        style="width: 55px; height: auto; margin: 0px;"
                    ),
                    H2("Burger Kong", style="color: #502314; margin: 0;"),
                    style="display: flex; align-items: center; gap: 10px;"
                ),
                Div(
                    Form(
                        Input(id="search", name="search", placeholder="Search products...",
                            style="""
                                background: #f8e3c2; 
                                border: 2px solid #502314; 
                                color: #502314; 
                                padding: 8px 12px; 
                                border-radius: 10px;
                                font-size: 16px;
                                outline: none;
                                height: 40px;
                                width: 250px;
                            """),
                        hx_get="/search",
                        target_id="results",
                        hx_trigger="keyup delay:500ms",
                        hx_preserve="true",
                        style="display: flex; align-items: center; justify-content: center; margin-top: 10px;"
                    ),
                    Div(
                        Button(
                            Img(src="https://i.imgur.com/Xyhfm0Q.png", style="width: 40px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;"),
                        Button(
                            Img(src="https://i.imgur.com/AcIDazc.png", style="width: 40px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;"),
                        Button(
                            Img(src="https://i.imgur.com/2eQjSEg.png", style="width: 40px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;"),
                        style="display: flex; align-items: center; gap: 5px; margin-left: 20px;" 
                    ),
                    style="color: #502314; font-size: 20px; font-weight: bold; display: flex; justify-content: flex-end; align-items: center;"
                ),
                style="display: flex; align-items: center; justify-content: space-between; align-items: center; width: 100%; gap: 15px;" 
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
                H3("Create Account", 
                   style="font-size: 32px; text-align: center; color: #502314; font-weight: bold; font-family: 'Arial', sans-serif; margin-top: 50px;"),
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
                        Label(Input(type="radio", id="title-mr", name="title", value="mr", required=True), " Mr.",
                              style="color: #502314; font-size: 18px; font-weight: bold;"),
                        Label(Input(type="radio", id="title-ms", name="title", value="ms", required=True), " Ms.",
                              style="color: #502314; font-size: 18px; font-weight: bold;"),
                        Label(Input(type="radio", id="title-mrs", name="title", value="mrs", required=True), " Mrs.",
                              style="color: #502314; font-size: 18px; font-weight: bold;"),
                        style="display: flex; gap: 10px; margin-bottom: 15px; align-items: center;"
                    ),
                    Div(
                        Input(type="text", id="firstname", name="firstname", placeholder="*Firstname", required=True,
                              style="color: #000; width: 47%; padding: 10px; border-radius: 5px; border: 1px solid #502314; background: #fff;"),
                        Input(type="text", id="lastname", name="lastname", placeholder="*Lastname", required=True,
                              style="color: #000; width: 47%; padding: 10px; border-radius: 5px; border: 1px solid #502314; background: #fff;"),
                        style="display: flex; justify-content: space-between; margin-bottom: 5px;"
                    ),
                    Div(
                        Input(type="text", id="mobile", name="mobile", placeholder="*Mobile no.", required=True,
                              style="color: #000; width: 47%; padding: 10px; border-radius: 5px; border: 1px solid #502314; background: #fff;"),
                        Input(type="date", id="birthdate", name="birthdate", placeholder="*Birth Day", required=True,
                              style="color: #000; width: 47%; padding: 10px; border-radius: 5px; border: 1px solid #502314; background: #fff;"),
                        style="display: flex; justify-content: space-between; margin-bottom: 5px;"
                    ),
                    Div(
                        Input(type="email", id="email", name="email", placeholder="*Email", required=True,
                              style="color: #000; width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #502314; background: #fff;"),
                        style="margin-bottom: 1px;"
                    ),
                    Div(
                        P("Password", style="color: #502314; text-align: left; font-size: 18px; font-weight: bold; margin-bottom: 3px;"),
                        Input(type="password", id="password", name="password", placeholder="Password", autocomplete="off",
                              style="color: #000; width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #502314; background: #fff;"),
                        style="margin-bottom: 1px;"
                    ),
                    Div(
                        P("Password Confirmation", style="color: #502314; text-align: left; font-size: 18px; font-weight: bold; margin-bottom: 3px;"),
                        Input(type="password", id="confirm_password", name="confirm_password", placeholder="Password", autocomplete="off",
                              style="color: #000; width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #502314; background: #fff;"),
                        style="margin-bottom: 5px;"
                    ),
                    Div(
                        Input(type="checkbox", id="confirm", name="confirm", required=True),
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
                    action="/make_register",
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

@app.post('/make_register')
def register(title: str, firstname: str, lastname: str, mobile: str, birthdate: str, confirm: bool, password: str, confirm_password: str):
    if str(password) != str(confirm_password):
        return H1("Password doesn't match"), Form(Button("back", type="submit"))
    else:
        new_user = server.Member(
            user_id = len(system.get_user_list()) + 1,
            name = firstname,
            tel = mobile,
            password = password,
            lastname = lastname
        )
        if system.register(new_user):
            # Update the global variable in watch_and_seedetail
            server.current_user_id = new_user.get_id()
            return RedirectResponse("/home")
        else: 
            return H1("Registration failed: Username already exists.")

@app.get('/login')
def login(username: str, password: str):
    status, user = system.check_password(username, password)
    if not status:
        return H1("Access denied")
    if isinstance(user, Admin):
        return RedirectResponse("/admin")
    else:
        return RedirectResponse("/home")

serve()
