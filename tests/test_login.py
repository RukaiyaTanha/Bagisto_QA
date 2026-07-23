# tests/test_login.py
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import config


def test_admin_login_success(driver):
    login_page = LoginPage(driver)
    login_page.login(config.ADMIN_EMAIL, config.ADMIN_PASSWORD)

    wait = WebDriverWait(driver, config.DEFAULT_TIMEOUT)
    wait.until(EC.title_contains("Dashboard"))

    dashboard_page = DashboardPage(driver)
    assert "Dashboard" in dashboard_page.get_title()


def test_admin_login_wrong_password(driver):
    login_page = LoginPage(driver)
    login_page.login(config.ADMIN_EMAIL, "wrongpassword123")

    time.sleep(2)
    assert "Sign In" in driver.title