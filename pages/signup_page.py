from pages.base_page import BasePage

class SignupPage(BasePage):

    @property
    def signup_name_input(self):
        return self.locator('[data-qa="signup-name"]')

    @property
    def signup_email_input(self):
        return self.locator('[data-qa="signup-email"]')

    @property
    def signup_button(self):
        return self.locator('[data-qa="signup-button"]')

    @property
    def title_mr_radio(self):
        return self.locator('[id="id_gender1"]')

    @property
    def title_mrs_radio(self):
        return self.locator('[id="id_gender2"]')

    @property
    def password_input(self):
        return self.locator('[data-qa="password"]')

    @property
    def days_dropdown(self):
        return self.locator('[data-qa="days"]')

    @property
    def months_dropdown(self):
        return self.locator('[data-qa="months"]')

    @property
    def years_dropdown(self):
        return self.locator('[data-qa="years"]')

    @property
    def newsletter_checkbox(self):
        return self.locator('[id="newsletter"]')

    @property
    def offers_checkbox(self):
        return self.locator('[id="optin"]')

    @property
    def first_name_input(self):
        return self.locator('[data-qa="first_name"]')

    @property
    def last_name_input(self):
        return self.locator('[data-qa="last_name"]')

    @property
    def address_input(self):
        return self.locator('[data-qa="address"]')

    @property
    def country_dropdown(self):
        return self.locator('[data-qa="country"]')

    @property
    def state_input(self):
        return self.locator('[data-qa="state"]')

    @property
    def city_input(self):
        return self.locator('[data-qa="city"]')

    @property
    def zipcode_input(self):
        return self.locator('[data-qa="zipcode"]')

    @property
    def mobile_number_input(self):
        return self.locator('[data-qa="mobile_number"]')

    @property
    def create_account_button(self):
        return self.locator('[data-qa="create-account"]')
    
    @property
    def continue_button(self):
        return self.by_role("link", "Continue")
    
    @property
    def existing_email_error(self):
        return self.by_text("Email Address already exist!")

    def continue_after_signup(self):
        self.click(self.continue_button)

    def start_signup_only(self, name: str, email: str):
        self.fill(self.signup_name_input, name)
        self.fill(self.signup_email_input, email)
        self.click(self.signup_button)
    
    def signup(
        self,
        name: str,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        address: str,
        country: str,
        state: str,
        city: str,
        zipcode: str,
        mobile_number: str,
        day: str = None,
        month: str = None,
        year: str = None,
        subscribe_newsletter: bool = False,
        receive_offers: bool = False
    ):
        self.fill(self.signup_name_input, name)
        self.fill(self.signup_email_input, email)
        self.click(self.signup_button)

        self.fill(self.password_input, password)

        if day:
            self.select_option(self.days_dropdown, value=day)
        if month:
            self.select_option(self.months_dropdown, value=month)
        if year:
            self.select_option(self.years_dropdown, value=year)

        if subscribe_newsletter:
            self.click(self.newsletter_checkbox)
        if receive_offers:
            self.click(self.offers_checkbox)

        self.fill(self.first_name_input, first_name)
        self.fill(self.last_name_input, last_name)
        self.fill(self.address_input, address)
        self.select_option(self.country_dropdown, label=country)
        self.fill(self.state_input, state)
        self.fill(self.city_input, city)
        self.fill(self.zipcode_input, zipcode)
        self.fill(self.mobile_number_input, mobile_number)

        self.click(self.create_account_button)