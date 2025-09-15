from pages.base_page import BasePage

class LoginPage(BasePage):

    @property
    def login_email_input(self):
        return self.locator('[data-qa="login-email"]')

    @property
    def login_password_input(self):
        return self.locator('[data-qa="login-password"]')

    @property
    def login_button(self):
        return self.locator('[data-qa="login-button"]')
    
    @property
    def login_error_message(self):
        return self.by_text("Your email or password is incorrect!")

    def login(self, email: str, password: str):
        try:
            self.fill(self.login_email_input, email)
            self.fill(self.login_password_input, password)
            self.click(self.login_button)
        except Exception as e:
            raise Exception(f"Failed to perform login with email '{email}': {e}")