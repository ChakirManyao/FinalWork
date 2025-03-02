from .base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):
    FILTER_CATEGORY = (By.XPATH, "//div[contains(text(), 'Категория')]/following-sibling::div//input")
    FILTER_PRICE_MIN = (By.NAME, "price_min")
    FILTER_PRICE_MAX = (By.NAME, "price_max")
    FILTER_AVAILABILITY = (By.XPATH, "//div[contains(text(), 'Наличие')]/following-sibling::div//input")
    FILTER_BINDING = (By.XPATH, "//div[contains(text(), 'Переплет')]/following-sibling::div//input")
    APPLY_FILTERS_BUTTON = (By.XPATH, "//button[contains(text(), 'Применить')]")
    PRODUCT_LIST = (By.CSS_SELECTOR, "div.product-item")

    def apply_filters(self, category, price_min, price_max, availability, binding):
        self.send_keys(self.FILTER_CATEGORY, category)
        self.send_keys(self.FILTER_PRICE_MIN, price_min)
        self.send_keys(self.FILTER_PRICE_MAX, price_max)
        self.send_keys(self.FILTER_AVAILABILITY, availability)
        self.send_keys(self.FILTER_BINDING, binding)
        self.click(self.APPLY_FILTERS_BUTTON)

    def select_product(self, index):
        products = self.driver.find_elements(*self.PRODUCT_LIST)
        products[index].click()