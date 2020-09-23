from .base_page import BasePage
from pages.locators import BasePageLocators
class BasketPage(BasePage):
    def guest_no_product_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.PRODUCT_IN_BASKET), "Basket is not empty!"

    def guest_message_in_basket_about_empty(self):
        assert self.is_element_present(*BasePageLocators.TEXT_BASKET_EMPTY), "No message about empty basket"

