import pytest
import json
from playwright.sync_api import sync_playwright
from pathlib import Path
from components.header import Header
from pages.login_page import LoginPage

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        choices=["chromium", "firefox", "webkit"],
        help="Choose which browser to run: chromium, firefox, or webkit",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=True,
        help="Run browser in headless mode (default is headless).",
    )
    parser.addoption(
        "--base-url",
        action="store",
        default="https://automationexercise.com",
        help="Base URL for the application under test.",
    )

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getoption("--base-url")

@pytest.fixture(scope="session")
def browser(pytestconfig):
    browser_name = pytestconfig.getoption("--browser")
    headless = pytestconfig.getoption("--headless")

    with sync_playwright() as p:
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=headless)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=headless)
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=headless)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser, base_url):
    context = browser.new_context(base_url=base_url)
    page = context.new_page()
    page.goto(base_url)

    try:
        consent_button = page.get_by_role("button", name="Consent")
        if consent_button.is_visible():
            consent_button.click()
    except Exception:
        pass

    yield page
    context.close()

@pytest.fixture(scope="session")
def test_data():
    file_path = Path(__file__).parent / "users.json"
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

@pytest.fixture(scope="function")
def logged_in_page(page, test_data):
    user = test_data["login"]["positive"][0] 

    header = Header(page)
    login_page = LoginPage(page)

    header.go_signup_login()

    login_page.login(user["email"], user["password"])

    yield page