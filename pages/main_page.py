from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    CITY_POPUP_CLOSE_BUTTON = (By.XPATH, "//button[contains(text(), 'Всё верно, закрыть')]")

    def close_city_popup(self):
        if self.is_element_present(self.CITY_POPUP_CLOSE_BUTTON):
            self.click(self.CITY_POPUP_CLOSE_BUTTON)

    def search_for_product(self, product_name):
        self.close_city_popup()  # Закрываем всплывающее окно перед поиском
        self.send_keys(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)