from fasthtml.common import *
class System:
    auto_book_id = 0
    def __init__(self):
        self.__book_list = []
        self.user_list = []
        self.__coupon_list = []
        self.__ordered_list = []
        self.__category_list = []
    def add_user(self,user):
        self.user_list.append(user)
        return "Success"
    def search_book_by_book_id(self,book_id):
        for each_book in self.__book_list:
            if book_id == each_book.get_book_id():
                return each_book
        return None
    def add_book_list(self,field):
        #field[0]:ชื่อ ,field[1]:สำนักพิมพ์,field[2]:วันที่พิมพ์,field[3]:ผู้แต่ง,field[4]:รายละเอียด,field[5]:ราคา,field[6]:หมวดหมู่
        book_new = Book(f"book_{self.auto_book_id}",field[0],field[1],field[2],field[3],field[4],field[5],0,field[7])
        book_new.edit_category(self.search_category_by_id(field[6]))
        self.__book_list.append(book_new)
        self.auto_book_id += 1
        return "Add Book Success"
    def search_category_by_id(self,cate_id):
        for each_category in self.__category_list:
            if cate_id == each_category.get_id_category():
                return each_category
        return None
    def add_category(self,id,name):
        self.__category_list.append(Category(id,name))
        return "Success"
    def show_book_list(self):
        return self.__book_list
    def show_category_list(self):
        return self.__category_list
    def edit_book(self,book_id,update_data):
        book_old = system.search_book_by_book_id(book_id)
        update_data[6] = self.search_category_by_id(update_data[6])
        # print(update_data[6])
        for field in update_data:
            if field == None or field == "" or field == 0:
                return "Error กรอกข้อมูลให้ครบ"
        if book_old.edit_detail(update_data) == "Success":
            return "Success"
    def del_book(self,book_id):
        book_to_del = system.search_book_by_book_id(book_id)
        self.__book_list.remove(book_to_del)
        return "Success"
    
class User:
    def __init__(self,id , name, email, phone_num, profile_picture=None):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__phone_numm = phone_num
        self.__profile_picture = profile_picture if profile_picture is not None else "default_img"
        self.__account = None
class Admin(User):
    def __init__(self,id , name, email, phone_num, profile_picture):
        super().__init__(id , name, email, phone_num, profile_picture)
        #field[0]:ชื่อ ,field[1]:สำนักพิมพ์,field[2]:วันที่พิมพ์,field[3]:ผู้แต่ง,field[4]:รายละเอียด,field[5]:ราคา,field[6]:หมวดหมู่
class Book:
    def __init__(self, id, name, publisher, publish_date, writer,detail_book, price, stock,url_img):
        self.__categlory = None
        self.__id = id
        self.__name = name
        self.__publisher = publisher
        self.__publish_date = publish_date
        self.__detail_book = detail_book
        self.__url_img = url_img
        self.__writer = writer
        self.__price = price
        self.__stock = stock
    def get_book_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_detail(self):
        return [self.__name,self.__publisher,self.__publish_date,self.__writer,self.__detail_book,self.__price,self.__categlory,self.__url_img]
    def edit_category(self,category):
        self.__categlory = category
    def edit_detail(self,update_data):
        self.__name = update_data[0]
        self.__publisher = update_data[1]
        self.__publish_date = update_data[2]
        self.__writer = update_data[3]
        self.__detail_book = update_data[4]
        self.__price = update_data[5]
        self.__categlory = update_data[6]
        self.__url_img = update_data[7]
        return "Success"
class Category:
    def __init__(self, id, name):
        self.__category_id = id
        self.__category_name = name
    def get_id_category(self):
        return self.__category_id
    def get_name_category(self):
        return self.__category_name
 
###############################################################
###############################################################
system = System()
#ัตัวอย่างว่าหนังสือมีการ add หลายเล่มแล้ว
system.add_category("cage_001","สังคมศาสตร์")
system.add_category("cage_002","คอมพิวเตอร์")
system.add_category("cage_003","วิทยาศาสตร์")
print("")
book_new_list = [
        ["Machine Learning Basics", "O'Reilly Media", "2022-06-15", "Alice Smith", "A guide to fundamental ML concepts.", 650.0, "cage_001",'https://marketplace.canva.com/EAFkZBeq9iA/1/0/1003w/canva-%E0%B8%AA%E0%B8%B5%E0%B8%99%E0%B9%89%E0%B8%B3%E0%B9%80%E0%B8%87%E0%B8%B4%E0%B8%99-%E0%B8%97%E0%B8%B1%E0%B8%99%E0%B8%AA%E0%B8%A1%E0%B8%B1%E0%B8%A2-%E0%B8%84%E0%B8%B9%E0%B9%88%E0%B8%A1%E0%B8%B7%E0%B8%AD%E0%B8%9D%E0%B8%B6%E0%B8%81%E0%B8%AD%E0%B8%9A%E0%B8%A3%E0%B8%A1-%E0%B8%9B%E0%B8%81%E0%B8%AB%E0%B8%99%E0%B8%B1%E0%B8%87%E0%B8%AA%E0%B8%B7%E0%B8%AD-%E0%B8%AD%E0%B8%B5%E0%B8%9A%E0%B8%B8%E0%B9%8A%E0%B8%81-CuMjaNbKuwI.jpg',2],
        ["Deep Learning for Coders", "Manning", "2021-09-20", "Francois Chollet", "Practical guide to deep learning.", 720.0, "cage_002",'https://marketplace.canva.com/EAFlIWj-ksM/1/0/1003w/canva-%E0%B8%AA%E0%B8%B5%E0%B8%9F%E0%B9%89%E0%B8%B2%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%AA%E0%B8%B5%E0%B8%99%E0%B9%89%E0%B8%B3%E0%B9%80%E0%B8%87%E0%B8%B4%E0%B8%99-%E0%B8%97%E0%B8%B1%E0%B8%99%E0%B8%AA%E0%B8%A1%E0%B8%B1%E0%B8%A2-%E0%B8%84%E0%B8%B9%E0%B9%88%E0%B8%A1%E0%B8%B7%E0%B8%AD%E0%B8%9B%E0%B8%90%E0%B8%A1%E0%B8%99%E0%B8%B4%E0%B9%80%E0%B8%97%E0%B8%A8-%E0%B8%9B%E0%B8%81%E0%B8%AB%E0%B8%99%E0%B8%B1%E0%B8%87%E0%B8%AA%E0%B8%B7%E0%B8%AD-%E0%B8%AD%E0%B8%B5%E0%B8%9A%E0%B8%B8%E0%B9%8A%E0%B8%84-4YyrtntUBxk.jpg',4],
        ["Data Science Handbook", "No Starch Press", "2020-11-10", "Jake VanderPlas", "Comprehensive guide for data scientists.", 480.0, "cage_001", 'https://www.การศึกษาไทย.com/wp-content/uploads/2022/03/%E0%B8%9B%E0%B8%81%E0%B8%AA%E0%B8%A7%E0%B8%A2-724x1024.jpeg',9],
        ["Algorithms Unlocked", "MIT Press", "2019-03-05", "Thomas Cormen", "Introduction to algorithms with examples.", 350.0, "cage_003",'https://marketplace.canva.com/EAEtceA3QlI/1/0/1003w/canva-%E0%B8%9B%E0%B8%81%E0%B8%AB%E0%B8%99%E0%B8%B1%E0%B8%87%E0%B8%AA%E0%B8%B7%E0%B8%AD-%E0%B8%AA%E0%B8%96%E0%B8%B2%E0%B8%9B%E0%B8%B1%E0%B8%95%E0%B8%A2%E0%B8%81%E0%B8%A3%E0%B8%A3%E0%B8%A1-%E0%B8%97%E0%B8%B1%E0%B8%99%E0%B8%AA%E0%B8%A1%E0%B8%B1%E0%B8%A2-%E0%B8%AA%E0%B8%B2%E0%B8%A1%E0%B9%80%E0%B8%AB%E0%B8%A5%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%A1-%E0%B8%AA%E0%B8%B5%E0%B8%AA%E0%B9%89%E0%B8%A1%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%AA%E0%B8%B5%E0%B8%A1%E0%B9%88%E0%B8%A7%E0%B8%87%E0%B9%80%E0%B8%82%E0%B9%89%E0%B8%A1-5zJo5bcUCl8.jpg',6],
        ["Python Crash Course", "No Starch Press", "2022-01-10", "Eric Matthes", "Best-selling Python programming book.", 500.0, "cage_002",'https://scontent.fbkk12-5.fna.fbcdn.net/v/t1.6435-9/76906353_2709992982373204_1416330981287133184_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=833d8c&_nc_ohc=MdwMBvKA1vkQ7kNvgGqFRNX&_nc_oc=AdixdAqjoGxU5AcysSffZHUyYN3xdQUwaUxWORrfbTA6tX265rKdQsHw4VesDRy0TRHe2WbSIwCV4MqZYcYnOuNc&_nc_zt=23&_nc_ht=scontent.fbkk12-5.fna&_nc_gid=AvA0GVFQ32S0rxu5iLxlkvE&oh=00_AYAqcIQbOQiVkophlYwtZV-aL-SOd30HoKzSbNLlxjHrwA&oe=67E68B77',7],
        ["Artificial Intelligence: A Guide", "Pearson", "2018-07-25", "Stuart Russell", "Introductory book to AI.", 680.0, "cage_003",'https://marketplace.canva.com/EAGOZKUTMGM/1/0/1003w/canva-%E0%B8%AA%E0%B8%B5%E0%B9%80%E0%B8%82%E0%B8%B5%E0%B8%A2%E0%B8%A7-%E0%B8%AA%E0%B8%B5%E0%B9%80%E0%B8%9A%E0%B8%88-%E0%B8%99%E0%B9%88%E0%B8%B2%E0%B8%A3%E0%B8%B1%E0%B8%81-%E0%B8%AA%E0%B8%99%E0%B8%B8%E0%B8%81%E0%B8%AA%E0%B8%99%E0%B8%B2%E0%B8%99-%E0%B8%A7%E0%B8%B4%E0%B8%8A%E0%B8%B2%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2%E0%B9%84%E0%B8%97%E0%B8%A2-%E0%B9%81%E0%B8%9A%E0%B8%9A%E0%B9%80%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%99-%E0%B8%AD%E0%B8%B5%E0%B8%9A%E0%B8%B8%E0%B9%8A%E0%B8%84-%E0%B8%9B%E0%B8%81%E0%B8%AB%E0%B8%99%E0%B8%B1%E0%B8%87%E0%B8%AA%E0%B8%B7%E0%B8%AD-WZrmlBSbNm8.jpg',12],
        ["Computer Networking", "Prentice Hall", "2020-08-15", "Andrew Tanenbaum", "Networking concepts for students.", 590.0, "cage_002",'https://marketplace.canva.com/EAE2Iac2z7E/1/0/1003w/canva-%E0%B8%9B%E0%B8%81%E0%B8%AB%E0%B8%99%E0%B8%B1%E0%B8%87%E0%B8%AA%E0%B8%B7%E0%B8%AD-%E0%B8%AD%E0%B8%B1%E0%B8%95%E0%B8%8A%E0%B8%B5%E0%B8%A7%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%A7%E0%B8%B1%E0%B8%95%E0%B8%B4-%E0%B8%AD%E0%B8%B1%E0%B8%88%E0%B8%89%E0%B8%A3%E0%B8%B4%E0%B8%A2%E0%B8%B0-%E0%B8%AA%E0%B8%B5%E0%B8%94%E0%B8%B3%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%AA%E0%B8%B5%E0%B9%80%E0%B8%AB%E0%B8%A5%E0%B8%B7%E0%B8%AD%E0%B8%87-OlGGhFyH0jM.jpg',12],
        ["Cybersecurity Essentials", "McGraw-Hill", "2021-05-01", "James Martin", "Essential concepts for cybersecurity.", 630.0, "cage_003",'https://winyuchon.com/wp-content/uploads/2023/05/99999.jpg',15],
        ["Big Data Analytics", "Springer", "2019-10-30", "Michael Stonebraker", "Comprehensive book on big data.", 750.0, "cage_001",'https://marketplace.canva.com/EAGLvYGfon4/1/0/1131w/canva-%E0%B8%AA%E0%B8%B5%E0%B8%9F%E0%B9%89%E0%B8%B2-%E0%B8%AA%E0%B8%B5%E0%B9%80%E0%B8%82%E0%B8%B5%E0%B8%A2%E0%B8%A7-%E0%B8%99%E0%B9%88%E0%B8%B2%E0%B8%A3%E0%B8%B1%E0%B8%81-%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%8C%E0%B8%95%E0%B8%B9%E0%B8%99-%E0%B8%99%E0%B8%B1%E0%B8%81%E0%B9%80%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%99-%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2%E0%B8%9B%E0%B8%81-%E0%B9%81%E0%B8%9A%E0%B8%9A%E0%B8%9D%E0%B8%B6%E0%B8%81%E0%B8%AB%E0%B8%B1%E0%B8%94-%E0%B9%80%E0%B8%AD%E0%B8%81%E0%B8%AA%E0%B8%B2%E0%B8%A3%E0%B8%82%E0%B8%99%E0%B8%B2%E0%B8%94-a4-b0mpSXLjTYE.jpg',200],
        ["The Pragmatic Programmer", "Addison-Wesley", "2020-03-10", "David Thomas", "Best practices for modern developers.", 550.0, "cage_002",'https://marketplace.canva.com/EAGJ5Q0FzMg/1/0/1131w/canva-%E0%B8%AA%E0%B8%B5%E0%B8%AA%E0%B9%89%E0%B8%A1-%E0%B8%99%E0%B9%88%E0%B8%B2%E0%B8%A3%E0%B8%B1%E0%B8%81-%E0%B8%AA%E0%B8%94%E0%B9%83%E0%B8%AA-%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2%E0%B8%9B%E0%B8%81-%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9A%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B8%9B%E0%B8%B4%E0%B8%94%E0%B9%80%E0%B8%97%E0%B8%AD%E0%B8%A1-%E0%B8%A7%E0%B8%B4%E0%B8%8A%E0%B8%B2%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2%E0%B9%84%E0%B8%97%E0%B8%A2-document-a4-Fe99JIxMIZA.jpg',10]
    ]
for book_new in book_new_list:
    if system.add_book_list(book_new) == "Error":
        print("Error")
admin = Admin(1,"naphat",'plengnapat23@gmail.com','0992975333','IMG')
books = system.show_book_list()





###############################################################
###############################################################
app, rt = fast_app()

@rt('/')
def get(request):
    return Titled(
        Head(
            Title('ระบบจัดการหนังสือ'),
        ),
        Body(
            H1('ระบบจัดการหนังสือ', style='text-align: center;'),
           Container(
            Button('เพิ่มหนังสือใหม่', cls='contrast', hx_get='/popup_add', hx_target="body", hx_swap="beforeend",style='text-align: center; background-color: #4CAF50; color: white; margin-right  :3%'),
            Style("""
            .popup_background {
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background: rgba(0, 0, 0, 0.5); display: flex;
                align-items: center; justify-content: center; z-index: 1000;
            }
            .popup_add-content {
                background: white; padding: 20px; border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.25);
                min-width: 300px; text-align: center;
            }
            .popup_background button {
                margin-top: 10px; padding: 5px 10px; border: none; background: #ff5b5b;
                color: white; border-radius: 5px; cursor: pointer;
            }
            .popup_background button:hover {
                background: #ff2b2b;
            }
        """),style="text-align:right;"),
            Table(
                Thead(  
                    Tr(
                        Th('ลำดับที่'),
                        Th('ชื่อหนังสือ'),
                        Th('สำนักพิมพ์'),
                        Th('ผู้แต่ง'),
                        Th('ราคา'),
                        Th('หมวดหมู่'),
                        Th('แก้ไข'),
                        Th('ลบ'),
                    )
                ),
                Tbody(
                        *[Tr(
                            Td(str(i+1), style="vertical-align: middle; text-align: center; font-weight: bold; padding: 10px; border-bottom: 1px solid #444;"),  # ลำดับที่
                            
                            # ✅ ชื่อหนังสือ + รูปภาพใน Td เดียวกัน (เรียงแนวตั้ง)
                            Td(
                                Div(
                                    books[i].get_detail()[0],  # ชื่อหนังสือ
                                    Br(),
                                    Img(src=books[i].get_detail()[7], width="160px", style="display: block; margin: 10px auto; border-radius: 8px; box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.2);"),  # ✅ ปรับให้ดูสวยขึ้น
                                    style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 5px; font-weight: bold;"
                                ),
                                style="vertical-align: top; padding: 15px; border-bottom: 1px solid #444;"
                            ),
                            
                            Td(books[i].get_detail()[1], style="vertical-align: middle; text-align: left; padding: 10px; border-bottom: 1px solid #444;"),  # สำนักพิมพ์
                            Td(books[i].get_detail()[3], style="vertical-align: middle; text-align: left; padding: 10px; border-bottom: 1px solid #444;"),  # ผู้แต่ง
                            Td(f"{books[i].get_detail()[5]:,.2f} บาท", style="vertical-align: middle; text-align: right; font-weight: bold; color: #FFD700; padding: 10px; border-bottom: 1px solid #444;"),  # ✅ ราคา (เพิ่มเครื่องหมาย , และปรับสี)
                            Td(books[i].get_detail()[6].get_name_category(), style="vertical-align: middle; text-align: left; padding: 10px; border-bottom: 1px solid #444;"),  # หมวดหมู่
                            
                            # ✅ ปุ่มแก้ไขและลบ (ปรับสไตล์ให้ดูสวยงามขึ้น)
                            Td(
                                Button('แก้ไข', 
                                    cls='contrast', 
                                    hx_get=f'/edit_popup/{str(books[i].get_book_id())}', 
                                    hx_target="body", hx_swap="beforeend",
                                    style='background-color: #FFD700; color: black; font-weight: bold; padding: 8px 15px; border-radius: 5px; box-shadow: 2px 2px 5px rgba(255, 215, 0, 0.3);'
                                ),
                                style="text-align: center; padding: 10px; border-bottom: 1px solid #444;"
                            ),
                            Td(
                                Button('ลบ', 
                                    cls='contrast', 
                                    hx_delete=f'/delete/{books[i].get_book_id()}', 
                                    target_id=f"item_{i}", 
                                    hx_confirm='คุณต้องการลบหนังสือหรือไม่?',
                                    style='background-color: #FF4C4C; color: white; font-weight: bold; padding: 8px 15px; border-radius: 5px; box-shadow: 2px 2px 5px rgba(255, 76, 76, 0.3);'
                                ),
                                style="text-align: center; padding: 10px; border-bottom: 1px solid #444;"
                            ),
                            id=f"item_{i}"
                        ) for i in range(len(books))]
                    )
            )
        ),
    )

@rt('/popup_add')
def get_popup():
    return Div(
        Div(
            H2("เพิ่มหนังสือใหม่"),
            Form(
                Div(Label("ชื่อหนังสือ",style="display: inline-block; width: 120px; text-align: right; margin-right: 10px; font-weight: bold; color: black;"),Input(type="text", id="book_name", required=True),style="display: flex; align-items: center; margin-bottom: 10px;"),
                Div(Label("ชื่อผู้แต่ง",style="display: inline-block; width: 120px; text-align: right; margin-right: 10px; font-weight: bold; color: black;"),Input(type="text", id="author", required=True),style="display: flex; align-items: center; margin-bottom: 10px;"),
                Div(Label("สำนักพิมพ์",style="display: inline-block; width: 120px; text-align: right; margin-right: 10px; font-weight: bold; color: black;"),Input(type="text", id="publisher", required=True),style="display: flex; align-items: center; margin-bottom: 10px;"),
                Div(Label("วันที่พิมพ์",style="display: inline-block; width: 120px; text-align: right; margin-right: 10px; font-weight: bold; color: black;"),Input(type="date", id="date", required=True),style="display: flex; align-items: center; margin-bottom: 10px;"),
                Div(Label("Url รูปภาพหนังสือ",style="display: inline-block; width: 120px; text-align: right; margin-right: 10px; font-weight: bold; color: black;"),Input(type="text", id="url", required=True),style="display: flex; align-items: center; margin-bottom: 10px;"),
                Div(
                    Label("รายละเอียดหนังสือ",style="font-weight: bold; color: black;"),
                    Textarea(
                        id="book_details",
                        required=True,
                        style="width: 100%; height: 200px; resize: both; border: 2px solid black; padding: 10px; font-size: 16px;"
                    ),
                    style="display: flex; flex-direction: column; gap: 10px; text-align: left; font-weight: bold; color: black;"
                ),
                Div(Label("หมวดหมู่หนังสือ",style="display: inline-block; width: 120px; text-align: right; margin-right: 10px; font-weight: bold; color: black;"),Select(*[Option(cagetory.get_name_category(),value=cagetory.get_id_category()) for cagetory in system.show_category_list()],id='cagetory'),style="display: flex; align-items: center; margin-bottom: 10px;"),
                Div(Label("ราคาหนังสือ",style="display: inline-block; width: 120px; text-align: right; margin-right: 10px; font-weight: bold; color: black;"),Input(type="number", id="price", required=True,min="10"),style="display: flex; align-items: center; margin-bottom: 10px;"),
                Button("เพิ่ม", type="submit", style="background-color: #4CAF50; color: white;"),
                Button("ยกเลิก", type="button", style="background-color: #FF4C4C; color: white;", onclick="document.getElementById('popup_add').remove()"),
                method="post",
                action="/add_book"
            ),  
            cls="popup_add-content"
        ),
        id="popup_add", cls="popup_background"
    )


@rt('/add_book')
def post(book_name:str,author:str,publisher:str,date:str,price:int,cagetory:str,book_details:str,url:str):
    # ["Machine Learning Essentials", "Packt", "2022-06-15", "Alice Smith", 650.0,"cage_001"]
    book_new = [book_name,publisher,date,author,book_details,price,cagetory,url]
    system.add_book_list(book_new)
    return RedirectResponse("/",status_code=303)

@rt('/edit_submit')
def post(book_name:str,author:str,publisher:str,date:str,price:int,cagetory:str,book_id:str,book_details:str,url:str):
    book_new = [book_name,publisher,date,author,book_details,price,cagetory,url]
    if system.edit_book(book_id,book_new) == "Success": 
        return RedirectResponse("/",status_code=303)
    else:
        "error"
# def post(d:dict): return d
@rt('/edit_popup/{book_id}')
def get_popup(book_id:str):
    book = system.search_book_by_book_id(book_id)
    book_detail = book.get_detail()
    category_options = [
        Option(category.get_name_category(), value=category.get_id_category(),
               selected=(category.get_id_category() == book_detail[6].get_id_category()))
        for category in system.show_category_list()
    ]
    return Div(
        Div(
            H2("แก้ไขหนังสือ"),
            Form(
                Div(Label("ชื่อหนังสือ",style="display: inline-block; width: 120px; text-align: right; margin-right: 10px; font-weight: bold; color: black;"),Input(type="text", id="book_name", required=True,value = book_detail[0]),style="display: flex; align-items: center; margin-bottom: 10px;"),
                Div(Label("ชื่อผู้แต่ง",style="display: inline-block; width: 120px; text-align: right; margin-right: 10px; font-weight: bold; color: black;"),Input(type="text", id="author", required=True,value = book_detail[3]),style="display: flex; align-items: center; margin-bottom: 10px;"),
                Div(Label("สำนักพิมพ์",style="display: inline-block; width: 120px; text-align: right; margin-right: 10px; font-weight: bold; color: black;"),Input(type="text", id="publisher", required=True,value = book_detail[1]),style="display: flex; align-items: center; margin-bottom: 10px;"),
                Div(Label("วันที่พิมพ์",style="display: inline-block; width: 120px; text-align: right; margin-right: 10px; font-weight: bold; color: black;"),Input(type="date", id="date", required=True,value = book_detail[2]),style="display: flex; align-items: center; margin-bottom: 10px;"),
                 Div(Label("Url รูปภาพหนังสือ",style="display: inline-block; width: 120px; text-align: right; margin-right: 10px; font-weight: bold; color: black;"),Input(type="text", id="url", required=True,value=book_detail[7]),style="display: flex; align-items: center; margin-bottom: 10px;"),
                Div(
                    Label("รายละเอียดหนังสือ", style="font-weight: bold; color: black;"),
                    Textarea(
                        book_detail[4],
                        id="book_details",
                        required=True,
                        style="width: 100%; height: 200px; resize: both; border: 2px solid black; padding: 10px; font-size: 16px;"
                    ),
                    style="display: flex; flex-direction: column; gap: 10px; text-align: left; font-weight: bold; color: black;"
                ),
                Div(Label("หมวดหมู่หนังสือ",style="display: inline-block; width: 120px; text-align: right; margin-right: 10px; font-weight: bold; color: black;"),Select(*category_options,id='cagetory'),style="display: flex; align-items: center; margin-bottom: 10px;"),
                Div(Label("ราคาหนังสือ",style="display: inline-block; width: 120px; text-align: right; margin-right: 10px; font-weight: bold; color: black;"),Input(type="number", id="price", required=True,value=int(book_detail[5]),min="10"),style="display: flex; align-items: center; margin-bottom: 10px;"),
                Hidden(id="book_id", value=book.get_book_id()),
                Button("บันทึก", type="submit", style="background-color: #4CAF50; color: white;"),
                Button("ยกเลิก", type="button", style="background-color: #FF4C4C; color: white;", onclick="document.getElementById('edit').remove()"),
                method="post",
                action="/edit_submit"
            ),  
            cls="popup_add-content"
        ),
        id="edit", cls="popup_background")

@rt('/delete/{book_id}')
def delete(book_id:str):
    system.del_book(book_id)
    return ""


serve()