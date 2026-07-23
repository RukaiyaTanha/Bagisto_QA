from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import config
import time
from utils.logger import setup_logger

logger = setup_logger()


class CustomersPage:

    EXPORT_BUTTON = (
        By.XPATH,
        "(//button[contains(normalize-space(),'Export')])[1]"
    )

    FORMAT_DROPDOWN = (
        By.NAME,
        "format"
    )

    CONFIRM_EXPORT_BUTTON = (
        By.XPATH,
        "(//button[contains(normalize-space(),'Export')])[2]"
    )

    CUSTOMER_CHECKBOX = (
        By.CSS_SELECTOR,
        "label[for='mass_action_select_record_1']"
    )


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            config.DEFAULT_TIMEOUT
        )


    def open(self):
        url = f"{config.ADMIN_URL}/customers"
        logger.info(f"Opening customers page: {url}")
        self.driver.get(url)



    def select_customer(self):

        logger.info("Selecting customer checkbox")

        checkbox = self.wait.until(
            EC.element_to_be_clickable(
                self.CUSTOMER_CHECKBOX
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            checkbox
        )

        time.sleep(1)



    def click_export(self):

        logger.info("Clicking Export button")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.EXPORT_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        time.sleep(2)



    def select_export_format(self, format_value):

        logger.info(
            f"Selecting export format: {format_value}"
        )

        dropdown = self.wait.until(
            EC.visibility_of_element_located(
                self.FORMAT_DROPDOWN
            )
        )

        Select(dropdown).select_by_value(
            format_value
        )

        time.sleep(1)



    def confirm_export(self):

        logger.info("Confirming export")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.CONFIRM_EXPORT_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        time.sleep(5)



    def export_customers(self, format_type):

        logger.info("Starting customer export")


        # Step 1: select customer
        self.select_customer()


        # Step 2: click first Export button
        self.click_export()


        # Step 3: select format
        self.select_export_format(
            format_type
        )


        # Step 4: click final Export button
        self.confirm_export()