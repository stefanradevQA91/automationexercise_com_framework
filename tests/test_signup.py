import pytest
from faker import Faker
from playwright.sync_api import expect
from components.header import Header
from pages.signup_page import SignupPage

fake = Faker()

@pytest.mark.signup
@pytest.mark.parametrize("with_optional", [False, True], ids=["required_only", "with_optional"])
def test_signup(page, with_optional):
    header = Header(page)
    signup_page = SignupPage(page)

    header.go_signup_login()

    kwargs = {
        "name": "Stefan",
        "email": fake.unique.email(),        
        "password": "Password123!",
        "first_name": "Stefan",
        "last_name": "Radev",
        "address": "Test street 123",
        "country": "Canada",
        "state": "Ontario",
        "city": "Toronto",
        "zipcode": "M5H2N2",
        "mobile_number": "0876112233",
    }

    if with_optional:
        kwargs.update({
            "day": "5",
            "month": "7",
            "year": "1992",
            "subscribe_newsletter": True,
            "receive_offers": True,
        })

    signup_page.signup(**kwargs)

    expect(page.get_by_text("Account Created!")).to_be_visible()

    assert "/account_created" in page.url

    signup_page.continue_after_signup()

    expect(header.logged_in_as_label).to_be_visible()
    expect(header.logged_in_as_label).to_contain_text(kwargs["name"])

@pytest.mark.signup
def test_signup_existing_email(page, test_data):
    header = Header(page)
    signup_page = SignupPage(page)

    header.go_signup_login()

    existing_email = test_data["login"]["positive"][0]["email"]

    signup_page.start_signup_only(name="Stefan", email=existing_email)

    expect(signup_page.existing_email_error).to_be_visible()

def test_signup_empty_required_fields(page):
    header = Header(page)
    signup_page = SignupPage(page)

    header.go_signup_login()

    signup_page.signup_button.click()

    validation_message = signup_page.signup_name_input.evaluate("el => el.validationMessage")
    assert validation_message.strip() != "", "Expected browser validation message for empty Name field"

    signup_page.signup_name_input.fill("Stefan")
    signup_page.signup_button.click()

    validation_message = signup_page.signup_email_input.evaluate("el => el.validationMessage")
    assert validation_message.strip() != "", "Expected browser validation message for empty Email field"

@pytest.mark.signup
def test_signup_account_info_required_fields(page):
    email = fake.unique.email()

    header = Header(page)
    signup_page = SignupPage(page)

    header.go_signup_login()

    signup_page.start_signup_only("Stefan", email)

    required_fields = [
    (signup_page.password_input, "Password"),
    (signup_page.first_name_input, "First Name"),
    (signup_page.last_name_input, "Last Name"),
    (signup_page.address_input, "Address"),
    (signup_page.state_input, "State"),
    (signup_page.city_input, "City"),
    (signup_page.zipcode_input, "Zipcode"),
    (signup_page.mobile_number_input, "Mobile Number"),
]

    for field, field_label in required_fields:
        signup_page.create_account_button.click()

        validation_message = field.evaluate("el => el.validationMessage")
        assert validation_message.strip() != "", f"Expected browser validation message for {field_label}"

        if field_label == "Password":
            field.fill("Password123!")
        elif field_label == "Zipcode":
            field.fill("1000")
        elif field_label == "Mobile Number":
            field.fill("0897661122")
        else:
            field.fill("Test Value")