# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from utils.screenshot import take_screenshot
from utils.logger import setup_logger

logger = setup_logger()


@pytest.fixture
def driver():

    import os

    download_dir = os.path.abspath("downloads")

    options = webdriver.ChromeOptions()

    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }

    options.add_experimental_option(
        "prefs",
        prefs
    )

    drv = webdriver.Chrome(options=options)

    drv.maximize_window()

    yield drv

    drv.quit()

@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.login()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_contains("Dashboard")) # <-- THE FIX: wait for login to fully complete
    yield driver  # <-- no wait for Dashboard to actually finish loading!   


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver") or item.funcargs.get("logged_in_driver")

        if driver:
            screenshot_path = take_screenshot(driver, item.name)
            logger.error(f"TEST FAILED: {item.name} - Screenshot saved: {screenshot_path}")
            print(f"\nScreenshot saved: {screenshot_path}")

