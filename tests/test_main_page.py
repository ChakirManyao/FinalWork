import pytest
from pages.main_page import MainPage


def test_main_page_elements(driver):
    main_page = MainPage(driver)
    driver.get("https://www.bookvoed.ru")

    # Проверка отображения основных элементов
    assert main_page.is_logo_visible(), "Логотип не отображается"
    assert main_page.is_search_input_visible(), "Поле поиска не отображается"
    assert main_page.is_search_button_visible(), "Кнопка поиска не отображается"


def test_search_functionality(driver):
    main_page = MainPage(driver)
    driver.get("https://www.bookvoed.ru")

    # Проверка работы поиска
    main_page.search_for_product("Python")
    assert "Python" in driver.title, "Поиск не выполнен"