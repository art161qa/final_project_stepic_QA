from .base_page import BasePage
from pages.locators import LoginPageLocators
import pytest
import time
class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert 'login' in login_url, 'This page is not login page # реализуйте проверку на корректный url адрес'
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self, email, password):

        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        pass_field = self.browser.find_element(*LoginPageLocators.PASS_FIELD)
        pass_field.send_keys(password)
        pass_field2 = self.browser.find_element(*LoginPageLocators.PASS_FIELD2)
        pass_field2.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button_register.click()


