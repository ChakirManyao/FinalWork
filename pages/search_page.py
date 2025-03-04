from .base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):
    FILTER_BRAND = (By.XPATH, "//span[contains(text(), 'Бренд')]/following-sibling::div//input")
    FILTER_CATEGORY = (By.XPATH, "//div[contains(text(), 'Категория')]/following-sibling::div//input")
    FILTER_PRICE_MIN = (By.NAME, "Цена от")
    FILTER_PRICE_MAX = (By.NAME, "Цена до")
    FILTER_AVAILABILITY = (By.XPATH, "//div[contains(text(), 'Наличие')]/following-sibling::div//input")
    FILTER_BINDING = (By.XPATH, "//div[contains(text(), 'Переплет')]/following-sibling::div//input")
    APPLY_FILTERS_BUTTON = (By.XPATH, "//button[contains(text(), 'Применить')]")
    PRODUCT_LIST = (By.CSS_SELECTOR, "div.product-item")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "select.sort-dropdown")

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

    def are_filters_applied(self):
        """Проверяет, применены ли фильтры."""
        return self.is_element_present(self.PRODUCT_LIST)

    def sort_products_by_price(self):
        """Сортирует товары по цене."""
        self.select_dropdown_option(self.SORT_DROPDOWN, "price_asc")

    def are_products_sorted_by_price(self):
        """Проверяет, отсортированы ли товары по цене."""
        prices = [float(product.text.replace("₽", "").replace(",", "").strip()) for product in
                  self.driver.find_elements(*self.PRODUCT_PRICE)]
        return prices == sorted(prices)