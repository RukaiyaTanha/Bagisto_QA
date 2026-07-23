from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import setup_logger
import config

logger = setup_logger()


class SalesReportPage:

    START_DATE = (
        By.CSS_SELECTOR,
        "input[placeholder='Start Date']"
    )

    MONTH_DROPDOWN = (
        By.CSS_SELECTOR,
        "select.flatpickr-monthDropdown-months"
    )

    YEAR_FIELD = (
        By.CSS_SELECTOR,
        "input.cur-year"
    )


    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            config.DEFAULT_TIMEOUT
        )


    def open(self):

        url = f"{config.ADMIN_URL}/reporting/sales"

        logger.info(
            f"Opening sales report page: {url}"
        )

        self.driver.get(url)


    def open_start_date(self):

        logger.info(
            "Opening start date picker"
        )

        self.wait.until(
            EC.element_to_be_clickable(
                self.START_DATE
            )
        ).click()


    def select_month_year(self, month, year):

        logger.info(
            f"Selecting month {month}, year {year}"
        )

        month_dropdown = self.wait.until(
            EC.visibility_of_element_located(
                self.MONTH_DROPDOWN
            )
        )

        Select(month_dropdown).select_by_value(
            str(month)
        )


        year_field = self.wait.until(
            EC.visibility_of_element_located(
                self.YEAR_FIELD
            )
        )

        year_field.clear()
        year_field.send_keys(
            str(year)
        )


    def select_day(self, date_label):

        logger.info(
            f"Selecting date: {date_label}"
        )

        DAY = (
            By.CSS_SELECTOR,
            f"span.flatpickr-day[aria-label='{date_label}']"
        )

        self.wait.until(
            EC.element_to_be_clickable(
                DAY
            )
        ).click()