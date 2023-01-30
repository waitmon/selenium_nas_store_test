import time
from pages.catalogue_page import CataloguePage
from pages.cart_page import CartPage
from pages.order_page import OrderInfo


def test_nas_search_field(setup):
    search_field_input = CataloguePage(setup)
    search_field_input.go_to_url()
    search_field_input.search_input('Boris')
    search_field_input.click_search_button()
    search_field_input.get_current_url()
    search_field_input.click_search_result_item_1()
    search_field_input.click_cart_icon()

    cart_page = CartPage(setup)
    cart_page.title_artist_assertion()
    cart_page.title_record_assertion()
    cart_page.cart_final_price_assertion()
    cart_page.get_current_url()
    cart_page.click_checkout_button()

    order_page = OrderInfo(setup)
    order_page.get_current_url()
    order_page.click_continue_button_item_list()
    order_page.click_continue_button_delivery_region()
    order_page.get_pick_up_point_info()
    order_page.click_continue_button_delivery()
    order_page.click_payment_type()
    time.sleep(1)
    order_page.click_continue_button_payment()
    order_page.name_input('Ivan Ivanov')
    order_page.email_input('Ivan@test.rf')
    order_page.phone_input('+7123456789')
    order_page.scroll_to_top()
    search_field_input.click_catalogue_button()