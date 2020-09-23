from pages.base_page import BasePage
import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import time


@pytest.mark.parametrize('product_link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                          pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser, product_link):
    # product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_message_add_to_basket()
    # product_page.should_not_be_success_message()
    product_page.should_be_correct_name_of_product()
    product_page.should_be_message_cost()
    product_page.should_be_equal_cost()
    time.sleep(5)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.guest_cant_see_success_message_after_adding_product_to_basket()

def test_guest_cant_see_success_message(browser):
    # product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.guest_cant_see_success_message_after_adding_product_to_basket()

def test_message_disappeared_after_adding_product_to_basket(browser):
    # product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.message_disappeared_after_adding_product_to_basket()

@pytest.mark.login_test
class TestLoginPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.guest_go_to_basket_from_main_page()
    page.guest_no_product_in_basket()
    page.guest_message_in_basket_about_empty()




