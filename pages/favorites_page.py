from .base_page import BasePage
from selenium.webdriver.common.by import By

class FavoritesPage(BasePage):
    FAVORITES_ITEMS = (By.CSS_SELECTOR, "div.favorites-item")
    REMOVE_FROM_FAVORITES_BUTTON = (By.CSS_SELECTOR, "button.remove-favorite")

    def add_to_favorites(self):
        """Добавляет товар в избранное."""
        self.click((By.CSS_SELECTOR, "button.add-to-favorites"))

    def is_product_in_favorites(self):
        """Проверяет, добавлен ли товар в избранное."""
        return len(self.driver.find_elements(*self.FAVORITES_ITEMS)) > 0

    def remove_from_favorites(self):
        """Удаляет товар из избранного."""
        if self.is_product_in_favorites():
            self.click(self.REMOVE_FROM_FAVORITES_BUTTON)

    def is_favorites_empty(self):
        """Проверяет, пусто ли избранное."""
        return len(self.driver.find_elements(*self.FAVORITES_ITEMS)) == 0