from .base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    CART_ITEMS = (By.CSS_SELECTOR, "div.cart-item")  # Локатор для элементов корзины
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button.remove-item")  # Локатор кнопки удаления товара

    def is_cart_empty(self):
        """Проверяет, пуста ли корзина."""
        return len(self.driver.find_elements(*self.CART_ITEMS)) == 0

    def remove_product(self):
        """Удаляет товар из корзины."""
        if not self.is_cart_empty():
            self.click(self.REMOVE_BUTTON)

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)