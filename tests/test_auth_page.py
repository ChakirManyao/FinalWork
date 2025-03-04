import pytest
from pages.auth_page import AuthPage


def test_login(driver):
    auth_page = AuthPage(driver)
    driver.get("https://www.bookvoed.ru/login")

    # Проверка входа в систему
    auth_page.login("username", "password")
    assert auth_page.is_user_logged_in(), "Пользователь не авторизован"


def test_registration(driver):
    auth_page = AuthPage(driver)
    driver.get("https://www.bookvoed.ru/register")

    # Проверка регистрации нового пользователя
    auth_page.register("new_user", "email@example.com", "password")
    assert auth_page.is_registration_successful(), "Регистрация не выполнена"