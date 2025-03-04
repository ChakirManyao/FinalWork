import pytest
from pages.checkout_page import CheckoutPage


def test_checkout(driver):
    checkout_page = CheckoutPage(driver)
    driver.get("https://www.bookvoed.ru/checkout")

    # Проверка оформления заказа
    checkout_page.fill_checkout_form("Иван Иванов", "ул. Примерная, 123", "ivan@example.com")
    checkout_page.place_order()
    assert checkout_page.is_order_placed(), "Заказ не оформлен"