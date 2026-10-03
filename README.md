# Bagisto QA Automation Framework

UI test automation for the admin panel of [Bagisto](https://github.com/bagisto/bagisto), an open-source Laravel e-commerce platform. Built with Python, Selenium, and Pytest using the Page Object Model, and run through a Jenkins pipeline.

## Latest Results

| Metric | Value |
|---|---|
| Tests | 24 |
| Passed | 24 |
| Failed | 0 |
| Duration | 11 min 29 sec |
| Run | Jenkins build #8 (25 Jul 2026) |

The full HTML report is in [`report.html`](report.html).

## What Is Tested

| Area | Scenarios |
|---|---|
| Authentication | Admin login (valid and wrong password), logout, session invalid after logout |
| Products | Create (including booking product), data-driven creation (3 data sets), missing SKU validation, edit, description saved after reload, product type dropdown options, filter by status, search |
| Categories | Create, create and delete, pagination |
| Currencies | Delete confirmation popup (cancel), delete and recreate, cannot delete the last currency |
| Customers | Export customers to XLS |
| Reports | Sales report date filter |
| Navigation | Open storefront in a new tab |

## Tech Stack

- Python 3.10
- Selenium WebDriver
- Pytest, pytest-html
- Page Object Model
- Jenkins, GitHub Actions
- Postman (API tests, see `API/`)

## Project Structure

```
.github/workflows/   CI workflow
API/                 Postman API test collection
Documentation/       Test documentation
pages/               Page Objects
tests/               Test cases
test_data/           Test data for data-driven tests
utils/               Helper functions
screenshots/         Screenshots captured during test runs
conftest.py          Pytest fixtures
config.py            Environment configuration
pytest.ini           Pytest settings
Jenkinsfile          Jenkins pipeline
requirements.txt     Python dependencies
```

## Getting Started

**Prerequisites:** Python 3.10, Google Chrome, and a running Bagisto instance with an admin account.

```bash
# 1. Clone the repo
git clone https://github.com/RukaiyaTanha/Bagisto_QA.git
cd Bagisto_QA

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your Bagisto URL and admin credentials in config.py
#    BASE_URL = "[your Bagisto URL]"

# 4. Run all tests and generate an HTML report
pytest --html=report.html --self-contained-html
```

Run a single test file:

```bash
pytest tests/[test_file_name].py
```

## CI/CD

The `Jenkinsfile` defines the **Bagisto-SQA-Pipeline** job, which checks out the repo, installs dependencies, runs the Pytest suite, and publishes the HTML report. A GitHub Actions workflow is also included in `.github/workflows/`.

## Author

**Rukaiya Tanha**
[LinkedIn](https://www.linkedin.com/in/rukaiya-tanha-694b1720a) | [GitHub](https://github.com/RukaiyaTanha)
