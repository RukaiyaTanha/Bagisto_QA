# pages/categories_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import setup_logger
import config
import time

logger = setup_logger()


class CategoriesPage:
    NAME_FIELD = (By.ID, "name")
    POSITION_FIELD = (By.CSS_SELECTOR, "input[name='position']")
    DISPLAY_MODE_DROPDOWN = (By.ID, "display_mode")
    DESCRIPTION_IFRAME = (By.ID, "description_ifr")
    SLUG_FIELD = (By.ID, "slug")
    SAVE_BUTTON = (By.XPATH, "//button[contains(text(),'Save Category')]")
    DELETE_ICON = (By.CSS_SELECTOR, "span.icon-delete")
    AGREE_BUTTON = (By.XPATH, "//button[text()='Agree']")
    DISAGREE_BUTTON = (By.XPATH, "//button[text()='Disagree']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.DEFAULT_TIMEOUT)

    def open_create_page(self):
        url = f"{config.ADMIN_URL}/catalog/categories/create"
        logger.info(f"Opening Create Category page: {url}")
        self.driver.get(url)

    def open_categories_list(self):
        url = f"{config.ADMIN_URL}/catalog/categories"
        logger.info(f"Opening Categories list page: {url}")
        self.driver.get(url)

    def enter_name(self, name):
        logger.info(f"Entering category name: {name}")
        field = self.wait.until(EC.visibility_of_element_located(self.NAME_FIELD))
        field.clear()
        field.send_keys(name)

    def enter_position(self, position):
        logger.info(f"Entering position: {position}")
        field = self.driver.find_element(*self.POSITION_FIELD)
        field.clear()
        field.send_keys(position)

    def select_display_mode(self, value):
        logger.info(f"Selecting display mode: {value}")
        dropdown = self.driver.find_element(*self.DISPLAY_MODE_DROPDOWN)
        Select(dropdown).select_by_value(value)

    def check_filterable_attribute(self, attribute_id):
        logger.info(f"Checking filterable attribute: {attribute_id}")
        checkbox_label = self.driver.find_element(
            By.CSS_SELECTOR, f"label[for='{attribute_id}'].cursor-pointer.icon-uncheckbox"
        )
        checkbox_label.click()

    def enter_description(self, text):
        logger.info(f"Entering category description: {text}")
        iframe = self.wait.until(EC.presence_of_element_located(self.DESCRIPTION_IFRAME))

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", iframe)
        time.sleep(0.5)

        self.driver.switch_to.frame(iframe)

        body = self.driver.find_element(By.TAG_NAME, "body")
        try:
            body.click()
        except Exception:
            logger.info("Body click intercepted, falling back to JS click")
            self.driver.execute_script("arguments[0].click();", body)

        body.send_keys(text)
        time.sleep(1)

        self.driver.switch_to.default_content()

    def enter_slug(self, slug):
        logger.info(f"Entering slug: {slug}")
        field = self.driver.find_element(*self.SLUG_FIELD)
        field.clear()
        field.send_keys(slug)

    def click_save(self):
        logger.info("Clicking Save Category button")
        button = self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        time.sleep(0.5)
        button.click()

    def create_category(self, name, position, display_mode, attribute_id, description, slug):
        self.enter_name(name)
        self.enter_position(position)
        self.select_display_mode(display_mode)
        self.check_filterable_attribute(attribute_id)
        self.enter_description(description)
        self.enter_slug(slug)
        self.click_save()

    def click_delete_icon_for_category(self, category_name):
        logger.info(f"Clicking delete icon for category: {category_name}")
        row = self.driver.find_element(
            By.XPATH, f"//p[contains(text(),\"{category_name}\")]/ancestor::div[contains(@class,'row')][1]"
        )
        delete_icon = row.find_element(*self.DELETE_ICON)
        delete_icon.click()

    def click_agree(self):
        logger.info("Clicking Agree on confirmation popup")
        self.wait.until(EC.element_to_be_clickable(self.AGREE_BUTTON)).click()

    def click_disagree(self):
        logger.info("Clicking Disagree on confirmation popup")
        self.wait.until(EC.element_to_be_clickable(self.DISAGREE_BUTTON)).click()

    def is_category_present(self, category_name):
        try:
            self.wait.until(EC.presence_of_element_located(
                (By.XPATH, f"//p[contains(text(),\"{category_name}\")]")
            ))
            return True
        except:
            return False

    def is_category_absent(self, category_name):
        try:
            self.wait.until_not(EC.presence_of_element_located(
                (By.XPATH, f"//p[contains(text(),\"{category_name}\")]")
            ))
            return True
        except:
            return False
        
    
    NEXT_PAGE_BUTTON = (By.XPATH,"//span[contains(@class,'icon-sort-right')]/parent::div")


    def get_first_category_name(self):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "div.row.grid.items-center.gap-2\\.5.border-b")
                )
            )
            
            return element.text

        except Exception as e:
            logger.error(f"Could not get first category row: {e}")
            
            return ""


    def go_to_next_page(self):

        logger.info("Opening next page")
        
        first_row_before = self.get_first_category_name()
        
        button = self.wait.until(
            EC.element_to_be_clickable(
                self.NEXT_PAGE_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",button
        )

        self.wait.until(
            lambda d: self.get_first_category_name() != first_row_before
        )