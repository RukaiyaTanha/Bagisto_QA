# pages/currencies_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import setup_logger
import config

logger = setup_logger()


class CurrenciesPage:
    DELETE_ICON = (By.CSS_SELECTOR, "span.icon-delete")
    DISAGREE_BUTTON = (By.XPATH, "//button[text()='Disagree']")
    AGREE_BUTTON = (By.XPATH, "//button[text()='Agree']")
    CURRENCY_ROW_NAME = (By.XPATH, "//p[contains(text(),'United States Dollar')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.DEFAULT_TIMEOUT)

    def open(self):
        logger.info(f"Opening Currencies page: {config.CURRENCIES_URL}")
        self.driver.get(config.CURRENCIES_URL)

    def click_delete_icon(self):
        logger.info("Clicking delete icon on currency row")
        self.wait.until(EC.element_to_be_clickable(self.DELETE_ICON)).click()

    def click_disagree(self):
        logger.info("Clicking Disagree on confirmation popup")
        self.wait.until(EC.element_to_be_clickable(self.DISAGREE_BUTTON)).click()

    def click_agree(self):
        logger.info("Clicking Agree on confirmation popup")
        self.wait.until(EC.element_to_be_clickable(self.AGREE_BUTTON)).click()

    def is_currency_present(self):
        """Checks if 'United States Dollar' currency is listed, waiting for the table to load"""
        try:
            self.wait.until(EC.presence_of_element_located(self.CURRENCY_ROW_NAME))
            return True
        except:
            return False
        
    def is_currency_absent(self):
        """Waits until USD is confirmed GONE from the table (opposite check of is_currency_present)"""
        try:
            self.wait.until_not(EC.presence_of_element_located(self.CURRENCY_ROW_NAME))
            return True
        except:
            return False

    def create_currency(self, name, code_value):
        logger.info(f"Creating currency: {name} ({code_value})")
        self.wait.until(EC.element_to_be_clickable(self.CREATE_CURRENCY_BUTTON)).click()

        from selenium.webdriver.support.ui import Select
        name_field = self.wait.until(EC.visibility_of_element_located(self.CURRENCY_NAME_FIELD))
        name_field.send_keys(name)

        code_dropdown = self.driver.find_element(*self.CURRENCY_CODE_DROPDOWN)
        Select(code_dropdown).select_by_value(code_value)

        self.driver.find_element(*self.SAVE_CURRENCY_BUTTON).click()