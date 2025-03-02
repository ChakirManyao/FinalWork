import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_bookvoed(driver):
    main_page = MainPage(driver)
    search_page = SearchPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)

    # Шаг 1: Переход на сайт
    driver.get("https://www.bookvoed.ru")

    # Шаг 2: Закрытие всплывающего окна с выбором города (если оно есть)
    if main_page.is_element_present(main_page.CITY_POPUP_CLOSE_BUTTON):
        main_page.close_city_popup()

    # Шаг 3: Поиск товара
    main_page.search_for_product("Python")

    # Шаг 4: Применение фильтров
    search_page.apply_filters("Книги", "500", "1000", "В наличии", "Твердый")

    # Шаг 5: Выбор товара
    search_page.select_product(0)

    # Шаг 6: Добавление товара в корзину
    product_page.add_to_cart()

    # Шаг 7: Переход в корзину
    driver.get("https://www.bookvoed.ru/cart")

    # Шаг 8: Оформление заказа
    cart_page.proceed_to_checkout()

    # Проверка, что мы на странице оформления заказа
    assert "checkout" in driver.current_url