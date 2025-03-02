from .base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)