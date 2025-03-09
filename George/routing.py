from fasthtml.common import *
app, rt = fast_app(live=True)
import register
import server
import all_menu
import admin_product
import admin
if __name__ == "__routing__":
    rt.run()