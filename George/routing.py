from fasthtml.common import *
app, rt = fast_app(live=True)
import register
import server
import all_menu
import admin_product
import admin_coupon
import admin
import admin_view_member_order
import coupon_member
import view_cart
import select_address

if __name__ == "__routing__":
    rt.run()