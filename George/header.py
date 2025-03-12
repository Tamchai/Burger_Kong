Container(
        Div(
            Div(
                Div(
                    Form(Button(
                        Img(src="https://i.imgur.com/fCpADUO.png", style="width: 50px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;")),      
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
                        Form(
                            Button(
                            Img(src="https://i.imgur.com/SwkvgTW.png",style="width: 40px; height: auto; margin-right: 15px;"),
                            style="background: none; border: none; cursor: pointer;", type = "submit"), action = f"/select_address/{user_id}", method = "GET"),
                        Form(Button(
                        Img(src="https://i.imgur.com/Xyhfm0Q.png", style="width: 40px; height: auto;"),
                            style="background: none; border: none; cursor: pointer;", type = "submit"), action = "####", method = "GET"),
                        Form(Button(
                            Img(src="https://i.imgur.com/JZR6dA6.png", style="width: 45px; height: auto;"),
                                style="background: none; border: none; cursor: pointer;", type = "submit"), action = "/coupon_member", method = "GET"),
                        Form(Button(
                            Img(src="https://i.imgur.com/2eQjSEg.png", style="width: 45px; height: auto;"),
                                style="background: none; border: none; cursor: pointer;", type = "submit"), action = f"/view_cart/{user_id}", method = "POST"),
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
        )