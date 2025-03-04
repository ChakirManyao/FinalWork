import pytest
from pages.favorites_page import FavoritesPage


def test_add_to_favorites(driver):
    favorites_page = FavoritesPage(driver)
    driver.get("https://www.bookvoed.ru/product/12345")  # Замени на реальный URL товара

    # Проверка добавления товара в избранное
    favorites_page.add_to_favorites()
    assert favorites_page.is_product_in_favorites(), "Товар не добавлен в избранное"


def test_remove_from_favorites(driver):
    favorites_page = FavoritesPage(driver)
    driver.get("https://www.bookvoed.ru/favorites")

    # Проверка удаления товара из избранного
    favorites_page.remove_from_favorites()
    assert favorites_page.is_favorites_empty(), "Товар не удален из избранного"