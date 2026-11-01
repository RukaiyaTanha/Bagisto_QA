# pages/login_page.py
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import setup_logger
import config

logger = setup_logger()


class LoginPage:
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    SIGN_IN_BUTTON = (By.XPATH, "//button[@aria-label='Sign In']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.DEFAULT_TIMEOUT)

    def open(self):
        logger.info(f"Opening admin login page: {config.ADMIN_URL}")
        self.driver.get(config.ADMIN_URL)

    def enter_email(self, email):
        logger.info(f"Entering email: {email}")
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_FIELD)).send_keys(email)

    def enter_password(self, password):
        logger.info("Entering password: ****")
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    
    def click_sign_in(self):
        from selenium.common.exceptions import TimeoutException

        logger.info("Clicking Sign In button")
        try:
            button = self.wait.until(
                EC.element_to_be_clickable(self.SIGN_IN_BUTTON)
            )
            button.click()

        except TimeoutException:
            os.makedirs("screenshots", exist_ok=True)

            self.driver.save_screenshot(
                "screenshots/login_button_not_found.png"
            )

            with open(
                "screenshots/login_page.html",
                "w",
                encoding="utf-8"
            ) as file:
                file.write(self.driver.page_source)

            logger.error(f"Current URL: {self.driver.current_url}")
            logger.error(f"Page title: {self.driver.title}")

            raise AssertionError(
                "Sign In button was not found. "
                "Check screenshots/login_page.html"
            )


    def login(self, email=None, password=None):
        self.open()
        self.enter_email(email or config.ADMIN_EMAIL)
        self.enter_password(password or config.ADMIN_PASSWORD)
        self.click_sign_in()