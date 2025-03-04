from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    LOGO = (By.CSS_SELECTOR, "div.logo")  # Локатор логотипа
    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    CITY_POPUP_CLOSE_BUTTON = (By.CSS_SELECTOR, "button.ui-button.ui-button--size-m.ui-button--fullwidth.ui-button--color-primary-blue.app-location-city-approve__button-accept")

    def close_city_popup(self):
        try:
            print("Пытаемся закрыть всплывающее окно...")
            # Проверяем, есть ли iframe
            iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
            if iframes:
                self.driver.switch_to.frame(iframes[0])  # Переключаемся на первый iframe

            # Ждем появления кнопки закрытия
            self.wait.until(EC.visibility_of_element_located(self.CITY_POPUP_CLOSE_BUTTON))
            print("Кнопка закрытия найдена, нажимаем...")
            # Закрываем окно
            self.click(self.CITY_POPUP_CLOSE_BUTTON)
            print("Всплывающее окно закрыто.")

            # Возвращаемся к основному контенту
            self.driver.switch_to.default_content()
        except Exception as e:
            print(f"Не удалось закрыть всплывающее окно: {e}")

    def is_logo_visible(self):
        """Проверяет, отображается ли логотип."""
        return self.is_element_present(self.LOGO)

    def is_search_input_visible(self):
        """Проверяет, отображается ли поле поиска."""
        return self.is_element_present(self.SEARCH_INPUT)

    def is_search_button_visible(self):
        """Проверяет, отображается ли кнопка поиска."""
        return self.is_element_present(self.SEARCH_BUTTON)

    def search_for_product(self, product_name):
        """Выполняет поиск товара."""
        self.send_keys(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)