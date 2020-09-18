from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    page = LoginPage(browser, link)
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()

