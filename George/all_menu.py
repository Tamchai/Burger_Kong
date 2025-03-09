from fasthtml.common import * 
from routing import app, rt
import server
system = server.system
count = 1
base_price = 0
def product_card(p): 
    menu_id = p.get_id()
    return Card(
        H3(p.get_name(), style="text-align: center; margin: 10px 0;"),
        Img(src=p.get_src(), alt="ภาพตัวอย่าง", style="width: 100px; height: 100px; display: block; margin: auto;"),
        P(f"${p.get_price()}", style="text-align: center; font-weight: bold;"),
        Form(
            Input(type="hidden", name = str(menu_id)),
            Button("SeeDetail", type="submit"),
            action=f"/detail/{p.get_id()}",
            method="get"
        ),
        style=(
            "min-width: 150px; "
            "max-width: 200px; "
            "height: 300px; "
            "padding: 10px; "
            "text-align: center; "
            "background: #fff; "
            "border-radius: 10px; "
            "box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); "
            "display: flex; "
            "flex-direction: column; "
            "justify-content: space-between;"
        )
    )

@app.get('/search')
def search(search: str):
    results = system.search_products_by_name(search)
    return Div(
        Grid(
            *[product_card(p) for p in results], 
            style="""
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 15px;
                justify-items: center;
                align-items: center;
                margin-top: 160px;
                padding: 20px;
                background-color: #f5ebdc;
            # """
        ),id="product-list"
    )

@app.get('/filter')
def filter(category: str):
    results = system.filter_category(category)
    if category == 'All Menu': 
        return Div(
                Grid(
                    *[product_card(p) for p in system.get_menu_list()],
                    style="""
                        display: grid;
                        grid-template-columns: repeat(4, 1fr);
                        gap: 15px;
                        justify-items: center;
                        align-items: center;
                        margin-top: 160px;
                        padding: 20px;
                        background-color: #f5ebdc;
                    """
                ),id="product-list")
    else :
        return Div(
            Grid(
                *[product_card(p) for p in results], 
                style="""
                    display: grid;
                    grid-template-columns: repeat(4, 1fr);
                    gap: 15px;
                    justify-items: center;
                    align-items: center;
                    margin-top: 160px;
                    padding: 20px;
                    background-color: #f5ebdc;
                # """
            ),id="product-list")

# user_id = session.get('current_user_id', None)
@rt("/home", methods=["GET","POST"])
def home():
    global count
    count = 1
    return Title("Burger Kong"),Container(
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
                            Img(src="https://i.imgur.com/JZR6dA6.png", style="width: 45px; height: auto;"),
                                style="background: none; border: none; cursor: pointer;"),
                        Button(
                            Img(src="https://i.imgur.com/2eQjSEg.png", style="width: 45px; height: auto;"),
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
            # H1(server.current_user_id),
            Form(Div(
                *[Button(text, name="category", value=text, id=text, 
                style="font-size: 36px; margin: 0 20px; font-weight: bold; color: #502314; background: none; border: none; cursor: pointer;")
                for text in ["All Menu", "Combo Set", "Burger", "Beverage", "Snack"]]
,
                style="""
                    position: absolute;
                    left: 0;
                    right: 0;
                    padding: 20px; 
                    background: #f8e3c2; 
                    margin-top: 40px; 
                    width: 100%; 
                    align-items: center;
                    display: flex;
                    justify-content: center;
                    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.5);
                """
            ),
                        hx_get="/filter",
                        target_id="results",
                        hx_trigger="click"),
            Div(
                Grid(
                    Div(*[product_card(p) for p in system.get_menu_list()],
                    style="""
                        display: grid;
                        grid-template-columns: repeat(4, 1fr);
                        gap: 15px;
                        justify-items: center;
                        align-items: center;
                        margin-top: 160px;
                        padding: 20px;
                        background-color: #f5ebdc;
                    """),
                ),
            id="results"),
            style="background: #f5ebdc; min-height: 100vh; display: flex; align-items: center; justify-content: center;"
        )
    )


@app.get("/detail/{menu_id}")
def detail(menu_id: int):
    global base_price
    menu = system.select_menu(menu_id)
    base_price = menu.get_price()
    if not menu:
        return "Menu item not found."
    return Title("Burger Kong"),Container(
        Div(
            Div(
                Div(
                    Button(
                        Img(src="https://i.imgur.com/fCpADUO.png", style="width: 50px; height: auto;"),
                        style="background: none; border: none; cursor: pointer;",
                        type = "button",
                        onclick = "history.back()"
                    ),
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
            Div(
                Div(
                    Div(
                        Img(
                            src=menu.get_src(),
                            height="500px",
                            width="500px",
                            style="border-radius: 10px; padding: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);"
                        ),
                        Div(
                            H1(menu.get_name(), style="color: #502314; font-size: 28px; font-weight: bold;"),
                            Hr(style="border: 1px solid #502314; opacity: 0.5; width: 100%;"),
                               P(menu.get_details(), style="color: #502314; font-size: 18px;"),
                            style="margin-top: 20px; width: 100%; display: flex; flex-direction: column; align-items: left;"
                        ),
                        style="width: 50%; display: flex; flex-direction: column; align-items: left; padding: 20px;"
                    ),
                    Div(
                        H4("Add on", Class="section-title", style="color: #502314; font-size: 24px; font-weight: bold; "),                            
                        Form(
                            Div(
                                Label(CheckboxX(id="More_Patty", name="More_Patty", value="More_Patty", hx_post="/update_price", hx_target="#price", hx_trigger="change" , hx_swap="innerHTML" ),"More Patty +1$" , style="color: #502314; font-size: 18px; font-weight: bold;"),
                                Label(CheckboxX(id="Bacon", name="Bacon", value="Bacon",hx_post="/update_price", hx_target="#price", hx_trigger="change" , hx_swap="innerHTML"),"Bacon +0.75$" ,  style="color: #502314; font-size: 18px; font-weight: bold;"),
                                Label(CheckboxX(id="More_Cheese", name="More_Cheese", value="More_Cheese", hx_post="/update_price",hx_trigger="change" , hx_target="#price", hx_swap="innerHTML"), "More Cheese +0.5$", style="color: #502314; font-size: 18px; font-weight: bold;")
                            ),
                            Hr(style="border: 1px solid #000; opacity: 0.5;"),
                            Div(
                                Span("Quantity", Class="section-title", style="color: #502314; font-size: 22px; font-weight: bold;"),
                                Div(
                                    Button("-", hx_post="/decrement", hx_target="#count-container", hx_swap="innerHTML", Class="PMBtn",
                                            style="""
                                                background: transparent; 
                                                border: none; 
                                                color: #502314;
                                                font-size: 28px;
                                                width: 40px; 
                                                height: 40px;
                                                display: flex;
                                                align-items: center;
                                                justify-content: center;
                                                margin: 0;
                                                padding: 0;
                                                cursor: pointer;
                                                font-family: 'Arial', sans-serif !important;
                                            """),
                                    Div(
                                        Span(f"{count}", id="count", Class="PMNumber", style="margin: 0 1px; font-size: 22px; font-weight: bold; font-family: inherit;"),
                                        Input(type="hidden" ,name="count" ,id="count-input", value=f"{count}"),
                                        id="count-container"
                                    ),
                                    Button("+", hx_post="/increment", hx_target="#count-container", hx_swap="innerHTML" ,Class="PMBtn",
                                        style="""
                                                all: unset;
                                                background: transparent; 
                                                border: none; 
                                                color: #502314;
                                                font-size: 28px;
                                                width: 40px; 
                                                height: 40px;
                                                display: flex;
                                                align-items: center;
                                                justify-content: center;
                                                margin: 0;
                                                padding: 0;
                                                cursor: pointer;
                                                font-family: 'Arial', sans-serif !important;
                                            """),
                                    style="color: #502314; display: flex; align-items: center; gap: 10px;"
                                ),
                                Class="plusminus",
                                style="display: flex; align-items: center; justify-content: space-between; width: 100%;"
                            ),
                            H3(f"Price - {base_price:.2f}$", id="price", style="color: #D00; margin: 10px 0px 5px 0px; text-align: center;"),
                            Button("Add to Cart", type="submit", Class="add-to-cart-btn",
                                   style="""
                                        font-weight: bold; 
                                        font-size: 20px; 
                                        background-color: #D00; 
                                        border: 1px solid #502314; 
                                        border-radius: 20px; 
                                        margin: 5px auto 0 auto;
                                    """),
                            method="post",
                            action=f"/save/{menu_id}",
                            style="margin-bottom: 0px; padding-bottom: 0px; display: flex; flex-direction: column;"
                        ),
                        style="""
                            width: 50%;
                            background: white;
                            padding: 10px 15px;
                            margin-top: 20px;
                            border-radius: 10px;
                            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
                            text-align: left;
                            height: 100%;
                            display: flex;
                            flex-direction: column;
                            gap: 8px;
                        """
                     ),
                    style="display: flex; justify-content: space-between; width: 90%; max-width: 1200px; margin: auto;"
                ),
                 style="display: flex; justify-content: space-between; align-items: flex-start; width: 90%; max-width: 1200px; margin: auto;"
            ),
            style="background: #f5ebdc; min-height: 100vh; display: flex; align-items: center; justify-content: center; margin-top: 5%; position: relative; "
        )
    )

# add to cart and send total price of menu 
@rt('/save/{menu_id}', methods=['POST'])
def post(More_Patty:str,Bacon:str,More_Cheese:str,count:int,menu_id : int):
    global current_user_id
    system.add_to_cart(server.current_user_id,menu_id,count,[More_Patty,Bacon,More_Cheese])
    count = 1
    return RedirectResponse("/home")

@app.post("/increment")
def increment():
    global base_price
    global count
    count += 1
    return update_count_and_price(base_price)

@app.post("/decrement")
def decrement():
    global count
    global base_price
    count = max(1, count - 1)
    return update_count_and_price(base_price)

def update_count_and_price(base_price):
    return f"""
        <span id="count" style="font-size: 22px; font-weight: bold; font-family: inherit;">{count}</span>
        <input type="hidden" name="count" id="count-input" value="{count}">
        <div hx-post="/update_price" hx-trigger="load" hx-target="#price" hx-swap="innerHTML"></div>
    """

@app.post("/update_price")
async def update_price(
    More_Patty: Optional[str] = Form(None),
    Bacon: Optional[str] = Form(None),
    More_Cheese: Optional[str] = Form(None),
    count: int = Form(1)
):  
    global base_price
    total_price = base_price * count  
    if More_Patty:
        total_price += 1.0 * count
    if Bacon:
        total_price += 0.75 * count
    if More_Cheese:
        total_price += 0.5 * count
    return f"Price - {total_price:.2f}$"

serve()