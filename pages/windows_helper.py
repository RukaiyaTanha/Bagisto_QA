# pages/windows_helper.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import setup_logger

logger = setup_logger()


class WindowsHelper:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_new_tab(self, url):
        """Opens a new tab with the given URL, simulating a real link that opens target='_blank'"""
        logger.info(f"Opening new tab with URL: {url}")
        main_window = self.driver.current_window_handle
        self.driver.execute_script(f"window.open('{url}', '_blank');")
        self.wait.until(EC.number_of_windows_to_be(2))
        return main_window

    def switch_to_new_window(self, main_window):
        """Switches focus to whichever window is NOT the main one"""
        for window in self.driver.window_handles:
            if window != main_window:
                self.driver.switch_to.window(window)
                logger.info(f"Switched to new window, title: {self.driver.title}")
                return
        raise Exception("No new window found to switch to")

    def close_current_and_return_to(self, main_window):
        """Closes the currently focused window, then switches back to main_window"""
        logger.info("Closing current window")
        self.driver.close()
        self.driver.switch_to.window(main_window)
        logger.info(f"Switched back to main window, title: {self.driver.title}")