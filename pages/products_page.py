from pages.base_page import BasePage
from typing import Tuple

class ProductsPage(BasePage):
    
    @property
    def search_input(self):
        return self.locator("#search_product")

    @property
    def search_button(self):
        return self.locator("#submit_search")

    def search(self, query: str) -> None:
        self.fill(self.search_input, query)
        self.click(self.search_button)

    @property
    def results_container(self):
        return self.locator(".features_items")

    @property
    def product_cards(self):
        return self.results_container.locator(".product-image-wrapper")
    
    @property
    def added_modal(self):
        return self.locator(".modal-content")

    @property
    def view_cart_button(self):
        return self.by_role("link", "View Cart")

    @property
    def continue_shopping_button(self):
        return self.by_role("button", "Continue Shopping")

    def card_overlay(self, index: int = 0):
        return self.product_cards.nth(index).locator(".product-overlay .overlay-content")

    def overlay_name(self, index: int = 0):
        return self.card_overlay(index).locator("p")

    def overlay_price(self, index: int = 0):
        return self.card_overlay(index).locator("h2")

    def overlay_add_to_cart_btn(self, index: int = 0):
        return self.card_overlay(index).locator("a.add-to-cart")

    def show_overlay(self, index: int = 0) -> None:
        self.product_cards.nth(index).hover()
        self.element_to_be_visible(self.card_overlay(index))

    def get_overlay_name_price(self, index: int = 0) -> Tuple[str, str]:
        self.show_overlay(index)
        name = self.get_text(self.overlay_name(index))
        price_text = self.get_text(self.overlay_price(index))
        return name, price_text

    def add_product_to_cart(self, index: int = 0):
        self.product_cards.nth(index).hover()
        self.element_to_be_visible(self.card_overlay(index))

        self.click(self.overlay_add_to_cart_btn(index))

        self.element_to_be_visible(self.added_modal)
        self.click(self.view_cart_button)