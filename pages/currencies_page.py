# pages/currencies_page.py
import time
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
    CREATE_CURRENCY_BUTTON = (By.XPATH, "//button[contains(text(),'Create Currency')]")
    CURRENCY_CODE_FIELD = (By.NAME, "code")
    CURRENCY_NAME_FIELD = (By.NAME, "name")
    SAVE_CURRENCY_BUTTON = (By.XPATH, "//button[contains(text(),'Save Currency')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.DEFAULT_TIMEOUT)

    def open(self):
        logger.info(f"Opening Currencies page: {config.CURRENCIES_URL}")
        self.driver.get(config.CURRENCIES_URL)

    def click_delete_icon_for(self, currency_name):
        logger.info(f"Deleting currency: {currency_name}")
        locator = (By.XPATH, f"//p[contains(text(),'{currency_name}')]/parent::div//span[contains(@class,'icon-delete')]")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_disagree(self):
        logger.info("Clicking Disagree on confirmation popup")
        self.wait.until(EC.element_to_be_clickable(self.DISAGREE_BUTTON)).click()

    def click_agree(self):
        logger.info("Clicking Agree on confirmation popup")
        self.wait.until(EC.element_to_be_clickable(self.AGREE_BUTTON)).click()

    def is_currency_present(self, currency_name="United States Dollar"):
        try:
            self.wait.until(EC.presence_of_element_located(
                (By.XPATH, f"//p[contains(text(),\"{currency_name}\")]")
            ))
            return True
        except:
            return False

    def is_currency_absent(self, currency_name="United States Dollar"):
        try:
            self.wait.until_not(EC.presence_of_element_located(
                (By.XPATH, f"//p[contains(text(),\"{currency_name}\")]")
            ))
            return True
        except:
            return False

    def create_currency(self, name, code_value):
        logger.info(f"Creating currency: {name} ({code_value})")
        self.wait.until(EC.element_to_be_clickable(self.CREATE_CURRENCY_BUTTON)).click()

        name_field = self.wait.until(EC.visibility_of_element_located(self.CURRENCY_NAME_FIELD))
        name_field.send_keys(name)

        code_field = self.wait.until(EC.visibility_of_element_located(self.CURRENCY_CODE_FIELD))
        code_field.send_keys(code_value)

        save_button = self.driver.find_element(*self.SAVE_CURRENCY_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_button)
        time.sleep(0.5)
        try:
            save_button.click()
        except Exception:
            logger.info("Save Currency click intercepted, falling back to JS click")
            self.driver.execute_script("arguments[0].click();", save_button)

    def click_delete_icon(self):
        logger.info("Deleting United States Dollar")
        locator = (By.XPATH, "//p[contains(text(),'United States Dollar')]/parent::div//span[contains(@class,'icon-delete')]")
        self.wait.until(EC.element_to_be_clickable(locator)).click()