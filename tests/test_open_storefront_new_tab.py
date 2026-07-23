# tests/test_open_storefront_new_tab.py
from pages.windows_helper import WindowsHelper
import config


def test_open_storefront_in_new_tab(logged_in_driver):
    windows_helper = WindowsHelper(logged_in_driver)

    admin_title_before = logged_in_driver.title
    assert "Dashboard" in admin_title_before   # confirm we're starting from the admin dashboard

    main_window = windows_helper.open_new_tab(config.BASE_URL)

    # Should now be 2 windows open
    assert len(logged_in_driver.window_handles) == 2

    windows_helper.switch_to_new_window(main_window)

    # Verify we're now looking at the storefront, NOT the admin panel
    assert "admin" not in logged_in_driver.current_url

    windows_helper.close_current_and_return_to(main_window)

    # Back on admin, should only be 1 window again
    assert len(logged_in_driver.window_handles) == 1
    assert "Dashboard" in logged_in_driver.title