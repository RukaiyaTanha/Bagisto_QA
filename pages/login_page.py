# pages/login_page.py
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
        logger.info("Clicking Sign In button")
        self.driver.find_element(*self.SIGN_IN_BUTTON).click()

    def login(self, email=None, password=None):
        self.open()
        self.enter_email(email or config.ADMIN_EMAIL)
        self.enter_password(password or config.ADMIN_PASSWORD)
        self.click_sign_in()