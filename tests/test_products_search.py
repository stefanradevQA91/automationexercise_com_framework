import re
import pytest
from components.header import Header
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from playwright.sync_api import expect

def _normalize_price(text: str) -> str:
    return re.sub(r"[^0-9.]", "", text or "").strip()

@pytest.mark.product
def test_task2_search_and_add_to_cart(logged_in_page):
    page = logged_in_page
    header = Header(page)
    products = ProductsPage(page)
    cart = CartPage(page)

    query = "t-shirt"
    index = 0  

    try:
        header.go_products()
        products.search(query)

        expect(page).to_have_url(f"https://automationexercise.com/products?search={query}")
        expect(products.results_container).to_be_visible()
        expect(products.product_cards.first).to_be_visible()

        name_before, price_text_before = products.get_overlay_name_price(index=index)
        price_before = _normalize_price(price_text_before)
        assert query in name_before.lower(), f"Expected '{query}' in result name."

        products.add_product_to_cart(index=index)
        expect(page).to_have_url("https://automationexercise.com/view_cart")
        cart.element_to_be_visible(cart.cart_table)

        cart_name = cart.first_product_name.inner_text()
        assert cart_name.strip().lower() == name_before.strip().lower(), \
            f"Cart name '{cart_name}' != selected '{name_before}'"

        cart_price_norm = _normalize_price(cart.first_product_price.inner_text())
        assert cart_price_norm == price_before, \
            f"Cart price '{cart_price_norm}' != selected '{price_before}'"
        assert "1" in cart.first_product_qty_cell.inner_text()
    finally:
        cart.remove_all_products()
        expect(cart.cart_is_empty_message).to_be_visible()

import pytest
from components.header import Header
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from playwright.sync_api import expect


@pytest.mark.product
def test_search_no_results(logged_in_page):
    page = logged_in_page
    header = Header(page)
    products = ProductsPage(page)
    cart = CartPage(page)

    query = "___no_such_product___"

    try:
        header.go_products()
        products.search(query)

        expect(products.product_cards.first).not_to_be_visible()

        header.go_cart()
        expect(cart.cart_rows.first).not_to_be_visible()
    finally:
        cart.remove_all_products()

@pytest.mark.product
def test_duplicate_add_increases_quantity(logged_in_page):
    page = logged_in_page
    header = Header(page)
    products = ProductsPage(page)
    cart = CartPage(page)

    header.go_products()
    products.search("t-shirt")
    products.add_product_to_cart(index=0)
    header.go_products()
    products.search("t-shirt")
    products.add_product_to_cart(index=0)

    expect(cart.first_product_qty_cell).to_contain_text("2")

    cart.remove_all_products()