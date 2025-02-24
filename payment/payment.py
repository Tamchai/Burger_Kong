from fasthtml.common import *

app, rt = fast_app(live=true)

@rt('/')
def get():
    return Div(
        Body(

        
        H3("สั่งอาหาร", style="""
            font-size:32px;
           text-align: center;
"""),
        
        # Name and Phone Number Input
        Form(
        Group(
            Label("ชื่อ", Input(type="text" ,id="name")),
            Label("เบอร์โทรศัพท์มือถือ",  Input(type="text" ,id="No")),
            Style="background-color:#f0f0f0:padding 15px; marginbottom:20px;"
        ),

        # Payment Method Selection
        H3("เลือกวิธีการชำระเงิน", cls="font-semibold mt-4"),
        Div(
            Label(Input(type="radio", name="payment", value="credit") , " บัตรเครดิต/เดบิต"),
            Label(Input(type="radio", name="payment", value="QRCODE"), " QRCODE"),
           
        ),

        # Submit Button
        Button("สั่งอาหาร", type="submit"),
        method="post",
        action="/submit",
        # style="background: #ffd6ce;",
        
        cls="max-w-md mx-auto p-6 bg-white rounded-lg shadow-md"
   ) ))
@rt("/submit")
def post(name: str, No: str,payment:str):
    return f"ยืนยัน: {name},{No},{payment}"
serve()
