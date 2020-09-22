from .base_page import BasePage
from pages.locators import ProductPageLocators



class ProductPage(BasePage):

    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_message_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), "Product is not in basket"
        assert True

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Success message is presented, but should not be"
    def should_be_correct_name_of_product(self):
        name_product_in_message = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_MESSAGE)
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        assert name_product.text == name_product_in_message.text, "Incorrect name of product"
        assert True
    def should_be_message_cost(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_COST), "Message about cost does not exist"
        assert True
    def should_be_equal_cost(self):
        cost_product = self.browser.find_element(*ProductPageLocators.COST_PRODUCT)
        cost_basket = self.browser.find_element(*ProductPageLocators.COST_BASKET)
        assert cost_product.text == cost_basket.text, 'Cost does not equal!'
        assert True
    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), 'Message exist'

    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_TO_BASKET)
