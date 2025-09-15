from pages.base_page import BasePage

class Header(BasePage):

    @property
    def home_link(self):
        return self.by_role("link", "Home")

    @property
    def products_link(self):
        return self.by_role("link", "Products")

    @property
    def cart_link(self):
        return self.by_role("link", "Cart")

    @property
    def signup_login_link(self):
        return self.by_role("link", "Signup / Login")

    @property
    def logout_link(self):
        return self.by_role("link", "Logout")

    @property
    def logged_in_as_label(self):
        return self.by_text("Logged in as")

    def logout(self):
        self.click(self.logout_link)
    
    def go_home(self):
        try:
            self.click(self.home_link)
        except Exception as e:
            raise Exception(f"Failed to navigate to Home: {e}")

    def go_products(self):
        try:
            self.click(self.products_link)
        except Exception as e:
            raise Exception(f"Failed to navigate to Products: {e}")

    def go_cart(self):
        try:
            self.click(self.cart_link)
        except Exception as e:
            raise Exception(f"Failed to navigate to Cart: {e}")

    def go_signup_login(self):
        try:
            self.click(self.signup_login_link)
        except Exception as e:
            raise Exception(f"Failed to navigate to Signup/Login: {e}")

    def expect_logged_in_as(self, username: str):
        try:
            self.element_to_be_visible(self.logged_in_as_label)
            text = self.get_text(self.logged_in_as_label)
            assert username in text, f"Expected username '{username}' in '{text}'"
        except Exception as e:
            raise Exception(f"Failed to verify logged in as '{username}': {e}")

    def expect_logged_out(self):
        try:
            self.element_to_be_visible(self.signup_login_link)
        except Exception as e:
            raise Exception(f"Failed to verify logged out state: {e}")