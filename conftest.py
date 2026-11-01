
import os
import pytest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


@pytest.fixture
def driver():

    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)

    options = webdriver.ChromeOptions()

    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }

    options.add_experimental_option("prefs", prefs)

    # GitHub Actions headless mode
    if os.getenv("GITHUB_ACTIONS") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    drv = webdriver.Chrome(options=options)

    if os.getenv("GITHUB_ACTIONS") != "true":
        drv.maximize_window()

    yield drv

    drv.quit()


@pytest.fixture
def logged_in_driver(driver):

    login_page = LoginPage(driver)
    login_page.login()

    WebDriverWait(driver, 10).until(
        EC.title_contains("Dashboard")
    )

    return driver
