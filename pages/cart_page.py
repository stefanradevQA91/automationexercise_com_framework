from pages.base_page import BasePage
from playwright.sync_api import expect

class CartPage(BasePage):

    @property
    def cart_table(self):
        return self.locator("#cart_info_table")

    @property
    def cart_rows(self):
        return self.cart_table.locator("tbody tr")

    @property
    def first_row(self):
        return self.cart_rows.first

    @property
    def first_product_name(self):
        return self.first_row.locator(".cart_description h4 a")

    @property
    def first_product_price(self):
        return self.first_row.locator(".cart_price p")

    @property
    def first_product_qty_input(self):
        return self.first_row.locator(".cart_quantity input")

    @property
    def first_product_qty_cell(self):
        return self.first_row.locator(".cart_quantity")
    
    @property
    def delete_buttons(self):
        return self.cart_table.locator("td.cart_delete a.cart_quantity_delete")
    
    @property
    def cart_is_empty_message(self):
        return self.by_text("Cart is empty!")
    
    def remove_all_products(self):
        while self.cart_rows.count() > 0:
            rows_before = self.cart_rows.count()
            self.click(self.delete_buttons.first)
            expect(self.cart_rows).to_have_count(rows_before - 1)