from fasthtml.common import *
app, rt = fast_app(live=True)
@rt('/')
def get():
    return Container(
        Div(
            Div(
                Div(
                    Img(src="/logocar.png", 
                        style="width: 55px; height: auto; margin: 0px;"
                    ),
                    H2("DRIVY", style="color: #B0E0E6; margin: 0;"),
                    style="display: flex; align-items: center; gap: 0px;"
                ),
                style="display: flex; justify-content: space-between; align-items: center; width: 100%;"
            ),
            style=""" 
                width: 100%; 
                background: #4682B4; 
                padding: 25px; 
                border-bottom: 2px solid #502314; 
                position: fixed; 
                top: 0; 
                left: 0; 
                width: 100%; 
                z-index: 1000;
            """
        ),
        Body( 
            Div(
                H3("LOGIN", style="font-size: 36px;text-align: center; color: #1C1C3B;"),
                Form(
                    Group(
                        Div(
                            Button("login", style="color: #1C1C3B; font-size: 18px; font-weight: bold;",type="button", id="login", name="olduser", value="login"),
                            style="display: flex; flex-direction: column; gap: 5px; width: auto;"
                        ),  
                            Div( 
                                Label("Username", style="color: #1C1C3B; font-size: 18px; font-weight: bold;"),
                                Input(type="text", id="Username", style="background: #fff; padding: 8px; border-radius: 15px; border: 1px solid #1C1C3B;"),
                                Label("Password", style="color: #1C1C3B; font-size: 18px; font-weight: bold;"), 
                                Input(type="text", id="Password", style="background: #fff; padding: 8px; border-radius: 15px; border: 1px solid #1C1C3B;"),
                                id="login-options",
                                style="display: none; background: #fff; padding: 8px; border-radius: 15px; border: 1px solid #1C1C3B;"    
                            ),
                        Div( 
                            Button("register", style="color: #1C1C3B; font-size: 18px; font-weight: bold;",type="button", id="register", name="newuser", value="regis"),
                            style="display: flex; flex-direction: column; gap: 5px; width: auto;"
                        ),  
                            Div(
                                Label("Username", style="color: #1C1C3B; font-size: 18px; font-weight: bold;"),
                                Input(type="text", id="Username", style="background: #fff; padding: 8px; border-radius: 15px; border: 1px solid #1C1C3B;"),
                                Label("Password", style="color: #1C1C3B; font-size: 18px; font-weight: bold;"), 
                                Input(type="text", id="Password", style="background: #fff; padding: 8px; border-radius: 15px; border: 1px solid #1C1C3B;"),
                                Label("Number", style="color: #1C1C3B; font-size: 18px; font-weight: bold;"),
                                Input(type="text", id="Number", style="background: #fff; padding: 8px; border-radius: 15px; border: 1px solid #1C1C3B;"),
                                id="register-options",
                                style="display: none; background: #fff; padding: 8px; border-radius: 15px; border: 1px solid #1C1C3B;"  
                            ),

                        style="display: flex; flex-direction: column; gap: 15px; background: #fff; padding: 15px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);"
                    ),
                        Button("submit", type="submit", style="background: #1C1C3B; color: white; font-weight: bold; padding: 10px 20px; border: none; border-radius: 20px; cursor: pointer; margin-top: 20px;"),
                        method="post",
                        action="/submit",
                        style="max-width: 500px; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);"
                    )
                ),
            style="background: #AEEEEE; padding: 20px; min-height: 100vh; margin-top: 80px;"
        ),
        # เพิ่ม <script> ที่จะแสดง/ซ่อน dropdown
        Script("""  
            document.getElementById('login').addEventListener('click', function() {
                var loginOptions = document.getElementById('login-options');
                var registerOptions = document.getElementById('register-options');
                loginOptions.style.display = 'block';
                registerOptions.style.display = 'none';
            });

            document.getElementById('register').addEventListener('click', function() {
                var loginOptions = document.getElementById('login-options');
                var registerOptions = document.getElementById('register-options');
                loginOptions.style.display = 'none';
                registerOptions.style.display = 'block';
            });     
                """)
    )
@rt("/submit")
def post(Username: str, Password: str, number: str):
    return f"ยืนยัน: {Username}, {Password}, {number}"

serve()