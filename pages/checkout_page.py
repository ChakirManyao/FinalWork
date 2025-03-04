from .base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):
    NAME_INPUT = (By.NAME, "name")
    ADDRESS_INPUT = (By.NAME, "address")
    EMAIL_INPUT = (By.NAME, "email")
    PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, "button.place-order")
    ORDER_CONFIRMATION = (By.CSS_SELECTOR, "div.order-confirmation")

    def fill_checkout_form(self, name, address, email):
        """Заполняет форму оформления заказа."""
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.ADDRESS_INPUT, address)
        self.send_keys(self.EMAIL_INPUT, email)

    def place_order(self):
        """Оформляет заказ."""
        self.click(self.PLACE_ORDER_BUTTON)

    def is_order_placed(self):
        """Проверяет, оформлен ли заказ."""
        return self.is_element_present(self.ORDER_CONFIRMATION)