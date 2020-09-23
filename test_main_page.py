from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     page.should_be_login_link()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_url()
#     login_page.should_be_login_form()
#     login_page.should_be_register_form()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser, link)
    page.open()
    page.guest_go_to_basket_from_main_page()
    page.guest_no_product_in_basket()
    page.guest_message_in_basket_about_empty()

