from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    # --- getters (берём данные со страницы) ---
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    # --- checks (принимают ожидаемые данные) ---
    def should_be_success_message_with_product_name(self, expected_name):
        actual_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert actual_name == expected_name, "Product name in success message is incorrect"

    def should_be_basket_total_equal_price(self, expected_price):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert basket_total == expected_price, "Basket total is not equal to product price"

