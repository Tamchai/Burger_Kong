from fasthtml.common import * 
from routing import app, rt
import server
from server import *
system = server.system
member = server.member


@app.get('/select_address/{current_user_id}', methods=["GET","POST"])
def select_address(current_user_id:int):
    user = system.search_user_by_id(current_user_id)
    address_list = user.get_address_list()
    print(address_list)
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
                            style="background: none; border: none; cursor: pointer;", type = "submit"), action = f"/select_address/{current_user_id}", method = "GET"),
                        Form(Button(
                        Img(src="https://i.imgur.com/Xyhfm0Q.png", style="width: 40px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;", type = "submit"), action = "####", method = "GET"),
                        Form(Button(
                            Img(src="https://i.imgur.com/JZR6dA6.png", style="width: 45px; height: auto;"),
                                style="background: none; border: none; cursor: pointer;", type = "submit"), action = f"/coupon_member/{current_user_id}", method = "GET"),
                        Form(Button(
                            Img(src="https://i.imgur.com/2eQjSEg.png", style="width: 45px; height: auto;"),
                                style="background: none; border: none; cursor: pointer;", type = "submit"), action = f"/view_cart/{current_user_id}", method = "POST"),
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
            *[Div(
                Div(
                    H3(address.get_name(), style="color: #502314; margin-bottom: 5px; text-align: left;"),
                    P(address.get_detail(), style="color: #502314; font-size: 16px; text-align: left;"),
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
            )for address in address_list],
            Div(
                Form(Button("Add new address", 
                    style="""display: flex; align-items: center; justify-content: center;
                             background: #fff; color: #D00000; padding: 10px 20px;
                             border-radius: 15px; margin-top: 20px; border: 1.5px solid #D00;
                             cursor: pointer;""",
                             type = "submit"
                ), action = f"/add_address/{current_user_id}", method = "GET",
                style="display: flex; justify-content: center; align-items: center; margin-top: 10px;"
            )),
            style="display: flex; flex-direction: column; align-items: center; min-height: 100vh; background: #f5ebdc; padding-bottom: 50px;"
        )
    )   
@app.post('/make_add_address/{current_user_id}')
def add(current_user_id:int, name:str, detail:str):
    user = system.search_user_by_id(current_user_id)
    user.add_address(name, detail)
    return RedirectResponse(f"/select_address/{current_user_id}")

@rt("/add_address/{current_user_id}", methods=["GET","POST"])
def add_address(current_user_id : int):
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
                            style="background: none; border: none; cursor: pointer;", type = "submit"), action = f"/select_address/{current_user_id}", method = "GET"),
                        Form(Button(
                        Img(src="https://i.imgur.com/Xyhfm0Q.png", style="width: 40px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;", type = "submit"), action = "####", method = "GET"),
                        Form(Button(
                            Img(src="https://i.imgur.com/JZR6dA6.png", style="width: 45px; height: auto;"),
                                style="background: none; border: none; cursor: pointer;", type = "submit"), action = f"/coupon_member/{current_user_id}", method = "GET"),
                        Form(Button(
                            Img(src="https://i.imgur.com/2eQjSEg.png", style="width: 45px; height: auto;"),
                                style="background: none; border: none; cursor: pointer;", type = "submit"), action = f"/view_cart/{current_user_id}", method = "POST"),
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
            Form(
                Label("Address name", style="color: #502314; font-size: 18px;"),
                Input(placeholder="Home, Office, etc.",type="text",id = "name", style="padding: 10px; width: 100%; margin-bottom: 10px;"),
                Label("Address detail", style="color: #502314; font-size: 18px;"),
                Textarea(placeholder="Street, City, Province, etc.",id="detail", style="padding: 10px; width: 100%; margin-bottom: 10px;"),
                Button("Add address",type="submit", style="width: 80%; background: #502314; color: #fff; padding: 10px 20px; border: none; border-radius: 15px; cursor: pointer;"),action = f"/make_add_address/{current_user_id}", method = "POST"
            )
        )
    )



serve()
