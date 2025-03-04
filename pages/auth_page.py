from .base_page import BasePage
from selenium.webdriver.common.by import By

class AuthPage(BasePage):
    LOGIN_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.login-button")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button.register-button")
    USER_ICON = (By.CSS_SELECTOR, "div.user-icon")

    def login(self, username, password):
        """Выполняет вход в систему."""
        self.send_keys(self.LOGIN_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_user_logged_in(self):
        """Проверяет, авторизован ли пользователь."""
        return self.is_element_present(self.USER_ICON)

    def register(self, username, email, password):
        """Регистрирует нового пользователя."""
        self.click(self.REGISTER_BUTTON)
        self.send_keys(self.LOGIN_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.send_keys((By.NAME, "email"), email)
        self.click(self.REGISTER_BUTTON)

    def is_registration_successful(self):
        """Проверяет, успешна ли регистрация."""
        return self.is_user_logged_in()