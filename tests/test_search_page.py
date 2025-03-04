import pytest
from pages.search_page import SearchPage


@pytest.mark.parametrize("category, price_min, price_max, availability, binding", [
    ("Книги", "500", "1000", "В наличии", "Твердый"),
    ("Канцтовары", "100", "500", "В наличии", "Мягкий"),
])
def test_apply_filters(driver, category, price_min, price_max, availability, binding):
    search_page = SearchPage(driver)
    driver.get("https://www.bookvoed.ru/search?q=Python")

    # Применение фильтров
    search_page.apply_filters(category, price_min, price_max, availability, binding)
    assert search_page.are_filters_applied(), "Фильтры не применены"


def test_sort_products(driver):
    search_page = SearchPage(driver)
    driver.get("https://www.bookvoed.ru/search?q=Python")

    # Проверка сортировки товаров
    search_page.sort_products_by_price()
    assert search_page.are_products_sorted_by_price(), "Товары не отсортированы по цене"