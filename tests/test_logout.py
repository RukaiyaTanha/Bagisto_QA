from pages.dashboard_page import DashboardPage


def test_logout(logged_in_driver):

    dashboard = DashboardPage(logged_in_driver)
    dashboard.logout()

    assert "/admin/login" in logged_in_driver.current_url