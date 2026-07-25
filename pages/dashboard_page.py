# pages/dashboard_page.py
from utils.logger import setup_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import setup_logger
import config

logger = setup_logger()


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            config.DEFAULT_TIMEOUT
        )

    def get_title(self):
        title = self.driver.title
        logger.info(f"Dashboard page title read as: {title}")
        return title
    
    LOGOUT_BUTTON = (
        By.XPATH,
        "//a[contains(@href,'logout')]"
    )

    PROFILE_BUTTON = (
        By.XPATH,
        "//button[contains(normalize-space(),'E')]"
    )


    def logout(self):

        logger.info("Opening profile menu")

        self.wait.until(
            EC.element_to_be_clickable(
                self.PROFILE_BUTTON
            )
        ).click()


        logger.info("Clicking logout button")

        self.wait.until(
            EC.element_to_be_clickable(
                self.LOGOUT_BUTTON
            )
        ).click()


        self.wait.until(
            EC.url_contains("login")
        )