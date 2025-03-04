from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1.product-title")  # Локатор названия товара
    PRODUCT_PRICE = (By.CSS_SELECTOR, "span.product-price")  # Локатор цены товара
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.add-to-cart")  # Локатор кнопки "Добавить в корзину"
    CART_ICON = (By.CSS_SELECTOR, "a.cart-icon")  # Локатор иконки корзины

    def is_product_name_visible(self):
        """Проверяет, отображается ли название товара."""
        return self.is_element_present(self.PRODUCT_NAME)

    def is_product_price_visible(self):
        """Проверяет, отображается ли цена товара."""
        return self.is_element_present(self.PRODUCT_PRICE)

    def add_to_cart(self):
        """Добавляет товар в корзину."""
        self.click(self.ADD_TO_CART_BUTTON)

    def is_product_in_cart(self):
        """Проверяет, добавлен ли товар в корзину."""
        self.click(self.CART_ICON)  # Переходим в корзину
        from pages.cart_page import CartPage  # Импортируем CartPage
        cart_page = CartPage(self.driver)  # Создаем экземпляр CartPage
        return not cart_page.is_cart_empty()  # Используем метод из CartPage
