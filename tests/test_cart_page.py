import pytest
from pages.cart_page import CartPage


def test_cart_functionality(driver):
    cart_page = CartPage(driver)
    driver.get("https://www.bookvoed.ru/cart")

    # Проверка отображения товаров в корзине
    assert cart_page.is_cart_empty() == False, "Корзина пуста"


def test_remove_product_from_cart(driver):
    cart_page = CartPage(driver)
    driver.get("https://www.bookvoed.ru/cart")

    # Проверка удаления товара из корзины
    cart_page.remove_product()
    assert cart_page.is_cart_empty(), "Товар не удален из корзины"