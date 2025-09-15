from components.header import Header
from pages.login_page import LoginPage
from playwright.sync_api import expect
import pytest

@pytest.mark.login
def test_login_valid_user(page, test_data):
    user = test_data["login"]["positive"][0]   

    header = Header(page)
    login_page = LoginPage(page)

    header.go_signup_login()
    login_page.login(user["email"], user["password"])

    header.expect_logged_in_as(user["email"])

@pytest.mark.login
@pytest.mark.parametrize("case_index", [0, 1], ids=["wrong_password", "non_existing_user"])
def test_login_invalid_user(page, test_data, case_index):
    user = test_data["login"]["negative"][case_index]

    header = Header(page)
    login_page = LoginPage(page)

    header.go_signup_login()
    login_page.login(user["email"], user["password"])

    expect(login_page.login_error_message).to_be_visible()

@pytest.mark.login
def test_logout(page, test_data):
    user = test_data["login"]["positive"][0]

    header = Header(page)
    login_page = LoginPage(page)

    header.go_signup_login()
    login_page.login(user["email"], user["password"])

    header.expect_logged_in_as(user["email"])
    header.logout()
    header.expect_logged_out()