import pytest
from pages.product_page import ProductPage


def test_product_details(driver):
    product_page = ProductPage(driver)
    driver.get("https://www.bookvoed.ru/product/12345")  # Замени на реальный URL товара

    # Проверка отображения информации о товаре
    assert product_page.is_product_name_visible(), "Название товара не отображается"
    assert product_page.is_product_price_visible(), "Цена товара не отображается"


def test_add_to_cart(driver):
    product_page = ProductPage(driver)
    driver.get("https://www.bookvoed.ru/product/12345")  # Замени на реальный URL товара

    # Проверка добавления товара в корзину
    product_page.add_to_cart()
    assert product_page.is_product_in_cart(), "Товар не добавлен в корзину"