# pages/products_page.py
from ast import keyword
from re import search
from time import time
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from utils.logger import setup_logger
import config

logger = setup_logger()


class ProductsPage:
    CREATE_PRODUCT_BUTTON = (By.XPATH, "//button[contains(text(),'Create Product')]")
    TYPE_DROPDOWN = (By.CSS_SELECTOR, "select[name='type']")
    FAMILY_DROPDOWN = (By.CSS_SELECTOR, "select[name='attribute_family_id']")
    SKU_FIELD = (By.CSS_SELECTOR, "input[name='sku']")
    SAVE_PRODUCT_BUTTON = (By.XPATH, "//button[contains(text(),'Save Product')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.DEFAULT_TIMEOUT)

    def open(self):
        logger.info(f"Opening Products page: {config.PRODUCTS_URL}")
        self.driver.get(config.PRODUCTS_URL)

    def click_create_product(self):
        logger.info("Clicking Create Product button")
        self.wait.until(EC.element_to_be_clickable(self.CREATE_PRODUCT_BUTTON)).click()

    def select_type(self, value):
        logger.info(f"Selecting Product Type: {value}")
        dropdown = self.wait.until(EC.visibility_of_element_located(self.TYPE_DROPDOWN))
        Select(dropdown).select_by_value(value)

    def select_family(self, value):
        logger.info(f"Selecting Attribute Family: {value}")
        dropdown = self.driver.find_element(*self.FAMILY_DROPDOWN)
        Select(dropdown).select_by_value(value)

    def enter_sku(self, sku):
        logger.info(f"Entering SKU: {sku}")
        self.driver.find_element(*self.SKU_FIELD).send_keys(sku)

    def click_save_product(self):
        logger.info("Clicking Save Product button")
        self.driver.find_element(*self.SAVE_PRODUCT_BUTTON).click()

    def create_quick_product(self, type_value, family_value, sku):
        """Combines the full quick-create modal flow into one call"""
        self.click_create_product()
        self.select_type(type_value)
        self.select_family(family_value)
        self.enter_sku(sku)
        self.click_save_product()

    def is_product_visible_by_name(self, product_name):
        """Checks if a product with this exact name appears anywhere on the current page"""
        try:
            element = self.driver.find_element(
                By.XPATH, f"//p[contains(text(),\"{product_name}\")]"
            )
            return element.get_attribute("textContent") != ""
        except:
            return False
        
    SEARCH_FIELD = (By.NAME,"search")

    def search_product(self, sku):
        logger.info(f"Searching product: {sku}") 
        search = self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_FIELD
            )
        )
        
        search.clear()
        search.send_keys(sku)
        search.send_keys("\n")

    def is_product_visible(self, keyword):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH,f"//*[contains(text(), '{keyword}')]")
                )
            )
            return element.is_displayed()
        except:
            return False
        
    def open_product_edit(self, product_id):
        logger.info(
            f"Opening edit page for product ID: {product_id}"
        )
        
        url = config.PRODUCT_EDIT_URL + str(product_id)
        self.driver.get(url)
    
    def get_current_url(self):
        return self.driver.current_url
    
    def create_product_without_sku(self, type_value, family_value):
        """Attempts to create a product WITHOUT entering SKU - should be blocked by validation"""
        self.click_create_product()
        self.select_type(type_value)
        self.select_family(family_value)
        # Deliberately skip enter_sku() here
        self.click_save_product()

    def is_still_on_products_page(self):
        """After a blocked save, we should NOT have navigated to an edit page"""
        return "/admin/catalog/products/edit/" not in self.driver.current_url
    
    from selenium.webdriver.support.ui import Select   # already imported at top, just confirming

    def get_all_type_options(self):
        """Opens the Create Product modal and returns all Product Type dropdown option texts"""
        self.click_create_product()
        dropdown = self.wait.until(EC.visibility_of_element_located(self.TYPE_DROPDOWN))
        select = Select(dropdown)
        return [option.text.strip() for option in select.options]
    
    FILTER_BUTTON = (By.XPATH,"//span[contains(text(),'Filter')]/parent::*")
    STATUS_DROPDOWN = (By.XPATH,"(//button[.//span[text()='Select']])[2]")
    ACTIVE_OPTION = (By.XPATH,"//li[normalize-space()='Active']")
    APPLY_FILTER_BUTTON = (By.XPATH,"//button[contains(text(),'Apply Filters')]")

    def click_filter(self):
        logger.info("Opening filter menu")

        button = self.wait.until(
            EC.visibility_of_element_located(self.FILTER_BUTTON)
        )
        
        self.driver.execute_script("arguments[0].click();", button)
        
        time.sleep(1)
        button.click()


    def select_status(self, status):
        logger.info(f"Selecting status: {status}")
        
        self.wait.until(
            EC.element_to_be_clickable(
                self.STATUS_DROPDOWN
            )
        ).click()
        
        time.sleep(1)

        if status.lower() == "active":
            self.wait.until(
                EC.element_to_be_clickable(
                    self.ACTIVE_OPTION
                )
            ).click()
            
            time.sleep(2)

    def filter_by_status(self, status):

        logger.info(f"Filtering products by status: {status}")

    # Open filter panel
        self.wait.until(
            EC.element_to_be_clickable(
                self.FILTER_BUTTON
            )
        ).click()

        time.sleep(1)


    # Open status dropdown
        self.wait.until(
            EC.element_to_be_clickable(
                self.STATUS_DROPDOWN
            )
        ).click()

        time.sleep(1)


    # Select Active
        if status.lower() == "active":

            self.wait.until(
                EC.element_to_be_clickable(
                    self.ACTIVE_OPTION
                )
            ).click()


        time.sleep(1)


    # Apply filters
        self.wait.until(
            EC.element_to_be_clickable(
                self.APPLY_FILTER_BUTTON
            )
        ).click()

        time.sleep(3)