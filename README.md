# Wiser Automation Framework

Scalable UI automation framework for [Automation Exercise](https://automationexercise.com).  
Built with **Playwright** + **Pytest** using the **Page Object Model (POM)** pattern.  
Includes modular components, structured test data, and GitHub Actions CI/CD.

---

## Project Structure

```
wiser_automation_framework/
│
├── components/           # reusable UI components
│   └── header.py
│
├── pages/                # Page Object classes
│   ├── base_page.py
│   ├── login_page.py
│   ├── signup_page.py
│   ├── products_page.py
│   └── cart_page.py
│
├── tests/                # Pytest test cases
│   ├── test_login.py
│   ├── test_signup.py
│   └── test_products_search.py
│
├── users.json            # dummy test data (login / signup)
├── conftest.py           # pytest fixtures (browser, page, test data)
├── pytest.ini            # pytest configuration and markers
├── requirements.txt      # Python dependencies
└── README.md             # project documentation
```
## Tech Stack
	-	Python 3.12+
	-	Playwright for Python
	-	Pytest
	-	Faker

## Installation & Setup

- 1.Clone the repository
git clone https://github.com/your-repo/wiser-automation-framework.git
cd wiser-automation-framework

- 2.Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

- 3.Install dependencies
pip install -r requirements.txt

- 4.Install Playwright browsers
python -m playwright install

## Running Tests

- Run all tests
pytest

- Run only login tests
pytest -m login

- Run a single test
pytest tests/test_products_search.py::test_task2_search_and_add_to_cart

## Pytest Markers

Defined in pytest.ini:
	-	login – login/logout tests
	-	signup – signup/registration tests
	-	product – product search & cart tests
	-   flaky - tests that are unstable/flaky

## Test Coverage

Task 1: User Registration
	- Positive flow:
		-	Positive registration with a new email.
	- Negative flows:
		-	Registration with an existing email.
		-	Browser validation messages for empty required fields.

Task 2: Search & Add to Cart
	- Positive flow:
        – Search for “t-shirt”.
        – Validate search results are displayed.
        – Capture product name and price from overlay.
        – Add product to cart and verify in Cart:
            * Product name matches the selected item.
            * Product price matches.
            * Quantity = 1.
        – Cart is cleared after each test.
    - Negative flows:
        – Search returns no results → cart remains empty.
		- Duplicate add of the same product

Task 3: Login & Logout
	- Positive flow:
		-	Successful login with all valid credentials.
		-	Successful login with all valid and optional (included) credentials.
	- Negative flows:	
		-	Negative login attempts (wrong password / invalid user).
		-	Logout validation (user redirected, “Signup / Login” link visible).
## CI/CD

This project uses **GitHub Actions** for continuous integration.

Workflow file: `.github/workflows/tests.yml`

Pipeline steps:
- Runs on every `push` or `pull_request` to the `main` branch.
- Sets up Python 3.12 and installs dependencies from `requirements.txt`.
- Installs Playwright browsers with required Linux dependencies.
- Executes all Pytest test cases (`pytest -q`).

You can check the latest pipeline runs in the [Actions tab](../../actions).