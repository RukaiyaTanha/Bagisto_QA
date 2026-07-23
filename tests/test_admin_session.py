# tests/test_admin_session.py

import config
from pages.dashboard_page import DashboardPage


def test_session_invalid_after_logout(logged_in_driver):

    dashboard = DashboardPage(logged_in_driver)

    # Logout
    dashboard.logout()

    # Verify redirected to login page
    assert "/admin/login" in logged_in_driver.current_url

    # Try opening a protected page directly
    logged_in_driver.get(
        f"{config.ADMIN_URL}/catalog/products"
    )

    # Session should be invalid
    assert "/admin/login" in logged_in_driver.current_url