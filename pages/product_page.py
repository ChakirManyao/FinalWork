from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(text(), 'Добавить в корзину')]")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)