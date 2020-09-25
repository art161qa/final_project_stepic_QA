from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    PRODUCT_IN_BASKET = (By.XPATH, "//div[@class='basket-items']")
    TEXT_BASKET_EMPTY = (By.XPATH, "//div[@id='content_inner']//p")
    BUTTON_BASKET = (By.XPATH, "//a[@class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.ID, "id_registration-email")
    PASS_FIELD = (By.ID, 'id_registration-password1')
    PASS_FIELD2 = (By.ID, 'id_registration-password2')
    BUTTON_REGISTER = (By.NAME, 'registration_submit')
class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_PRODUCT = (By.TAG_NAME, "h1")
    MESSAGE_ADD_TO_BASKET = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]")
    NAME_PRODUCT_IN_MESSAGE = (By.XPATH, "//div[@id='messages']//div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]//strong")
    MESSAGE_COST = (By.XPATH, "//div[@class='alertinner ']/p[1]")
    COST_PRODUCT = (By.XPATH, "//p[@class='price_color']")
    COST_BASKET = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    PRODUCT_IN_BASKET = (By.XPATH, "//div[@class='basket-items']")
    TEXT_BASKET_EMPTY = (By.XPATH, "//div[@id='content_inner']//p")
    BUTTON_BASKET = (By.XPATH, "//a[@class='btn btn-default']")


